$("#form-cadastrar-questao").on("submit", function(e) {
    e.preventDefault();
    let alternativas = $("#alternativas .alternativa");
    let alternativas_corretas = $("#alternativas .alternativa.correta");

    if (alternativas.length > 2 && alternativas_corretas.length > 0) {
        let form = $(this);

        // pega dados do form em array
        let formDataArray = form.serializeArray();
        let formDataObj = {};
        let alternativas = [];

        // move dados do array para um objeto
        $(formDataArray).each(function(i, field) {
            formDataObj[field.name] = field.value;
        });

        let counter = 0;
        form.find(".alternativa").each(function() {
            // ignorar primeira alternativa, pois ela não contém dados
            if (counter > 0) {
                let alternativa = $(this);

                alternativas.push(
                    JSON.stringify({
                        nome: alternativa.find(".nome").text(),
                        correta: alternativa.hasClass("correta")
                    })
                );
            }
            counter++;
        });

        let data = {
            modulo_uuid: form.data("modulo"),
            // nivel: formDataObj.nivel,
            verbo: formDataObj.verbo,
            tempo_para_responder: formDataObj.tempo_para_responder,
            sentenca: formDataObj.sentenca,
            descricao: CKEDITOR.instances["id_descricao"].getData(),
            alternativas: alternativas
        };

        $.ajax({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                }
            },

            url: `/modulo/${form.data('modulo')}/questao/${nivel}/adicionar/`,
            type: "POST",
            dataType: "JSON",
            data: data,

            success: function(data) {
                window.location.href = data.redirect_url;
            },
            error: function(data) {
                if (data.responseJSON.message) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Dados inválidos',
                        text: data.responseJSON.message
                    });
                }
                console.log("Houve um erro:", data);
            }
        });
    } else if (alternativas.length <= 2) {
        $(".invalid-alternativa")
            .show()
            .text("Adicione pelo menos duas alternativas");
    } else if (alternativas_corretas.length <= 0) {
        $(".invalid-alternativa")
            .show()
            .text("Marque pelo menos uma alternativa como correta");
    }
});
