var login_validator = {
    init: function() {
        login_validator.validator();
    },

    validator: function() {
        $(".ag_form_auth_login").submit(function(e) {
            if ($(".ag_input_username_login").val() == "") {
                if($(".ag_error_message_inputs_username_login").length) { $(".wrapper_name_input .ag_error_message_inputs_username_login").remove(); }
                if($(".ag_error_message_inputs_password_login").length) { $(".wrapper_password_input .ag_error_message_inputs_password_login").remove(); }
                $(".wrapper_name_input").append("<small class='ag_error_message_inputs_username_login'>Nombre requerido</small>");
                $(".ag_input_username_login").focus();
                return false;
            } else if ($(".ag_input_password_login").val() == "") {
                if($(".ag_error_message_inputs_password_login").length) { $(".wrapper_password_input .ag_error_message_inputs_password_login").remove(); }
                if ($(".ag_error_message_inputs_username_login").length) { $(".wrapper_name_input .ag_error_message_inputs_username_login").remove(); }
                $(".wrapper_password_input").append("<small class='ag_error_message_inputs_password_login'>Contraseña requerida</small>");
                $(".ag_input_password_login").focus();
                return false;
            }
            return true;

            if (!false) {
                e.preventDefault();
            }
        });
    }
};

$(document).ready(login_validator.init);