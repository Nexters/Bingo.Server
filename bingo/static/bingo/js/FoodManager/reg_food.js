$(document).ready(function() { 

	$("#submit_btn").click(function() {

		var food_name = $("#food_name");
		var food_icon1 = $("#food_icon1");
		var food_icon2 = $("#food_icon2");
		var food_rec_exp = $("#food_rec_exp");
		var food_extra_info = $("#food_extra_info");
		var no_mix_list = $("#no_mix_list");

		if (food_name.val() == "") {
			food_name.focus();
			return;
		}
		if (food_icon1.val() == "") {
			food_icon1.focus();
			return;
		}
		if (food_icon2.val() == "") {
			food_icon2.focus();
			return;
		}
		if (food_rec_exp.val() == "" || isNaN(food_rec_exp.val())) {
			food_rec_exp.focus();
			return;
		}

		$("#new_food_form").submit();
	});

});