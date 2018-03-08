$(document).ready(function() {
    // AJAX FOR SELECT DEPARTMENT AND FILL SE RELACIONA CON
    $('.se_relaciona_con_ajax_div').css('display', 'none');
    $('.ajax_relation_anchor').on('click', function(e){
        e.preventDefault();
        $('#ajaxRelationFilterModal').modal('show').find('.modal-body').load($(this).attr('href'));
    });

    $('#modal_ajax_button_filter_subsidies').click(function() {
        var dip_list = [];
        var gene_list = [];
        var gob_list = [];
        $("input[name='diputacion_ajax']:checked").each( function () {
           dip_list.push(parseInt($(this).val()));
        });
        $("input[name='generalitat_ajax']:checked").each( function () {
           gene_list.push(parseInt($(this).val()));
        });
        $("input[name='gobierno_ajax']:checked").each( function () {
           gob_list.push(parseInt($(this).val()));
        });

        $.ajax({
            method: 'GET',
            url: '{% url "myapp:ajax_se_relaciona_con" %}',
            data: {
                'diputacion_ajax': dip_list,
                'generalitat_ajax': gene_list,
                'gobierno_ajax': gob_list
            },
            dataType: 'json',
            success: function (data) {
                $('.se_relaciona_con_ajax_div').css('display', 'block');
                var ul_li = $('#id_se_relaciona_con');
                ul_li.text('');
                console.log(data);

                $.each(data, function(key, value){
                    ul_li.append("<li><label for='id_se_relaciona_con_"+key+"'><input type='checkbox' name='se_relaciona_con' value='"+value.pk+"' class='' id='id_se_relaciona_con_"+key+"'>"+value.fields['nombre']+"</label></li>");
                });
            }
        });
    });

    // $("#id_diputacion").change(function () {
    //     var select = $(this).val();
    //
    //     $.ajax({
    //         method: 'GET',
    //         url: '{% url "myapp:ajax_se_relaciona_con" %}',
    //         data: {
    //             'diputacion': select,
    //             'generalitat': 999,
    //             'gobierno': 999
    //         },
    //         dataType: 'json',
    //         success: function (data) {
    //             console.log(data);
    //         }
    //     });
    // });
    // $("#id_generalitat").change(function () {
    //     var select = $(this).val();
    //
    //     $.ajax({
    //         method: 'GET',
    //         url: '{% url "myapp:ajax_se_relaciona_con" %}',
    //         data: {
    //             'generalitat': select,
    //             'diputacion': 999,
    //             'gobierno': 999
    //         },
    //         dataType: 'json',
    //         success: function (data) {
    //             console.log(data);
    //         }
    //     });
    // });
    // $("#id_gobierno").change(function () {
    //     var select = $(this).val();
    //
    //     $.ajax({
    //         method: 'GET',
    //         url: '{% url "myapp:ajax_se_relaciona_con" %}',
    //         data: {
    //             'gobierno': select,
    //             'generalitat': 999,
    //             'diputacion': 999
    //         },
    //         dataType: 'json',
    //         success: function (data) {
    //             console.log(data);
    //         }
    //     });
    // });
});