$(document).ready(function() {

	$("#manager_id").focus();

	$("#manager_id").bind("keydown", function(e) {
		if (e.keyCode == 13) { // enter key
			$("#submit_btn").click();
		}
	});
	$("#password").bind("keydown", function(e) {
		if (e.keyCode == 13) { // enter key
			$("#submit_btn").click();
		}
	});

	$("#submit_btn").click(function() {
		
		var manager_id = $("#manager_id");
		var password = $("#password");

		if (manager_id.val() == "") {
			manager_id.focus();
			return;
		}
		if (password.val() == "") {
			password.focus();
			return;
		}

		var password_enc = $.sha256(password.val());
		password.val(password_enc);

		$("#login_form").submit();
	});

});