$(document).ready(function() {

	// $('#name').bind('input propertychange', function() {
	// 	validate();
	// });

	// $('#body').bind('input propertychange', function() {
	// 	validate();
	// });


	$('#form-submit').click(function(e) {
		e.preventDefault()
		var name = $("#name").val();
		var email = $('#email').val();
		var message = $('#message').val();

		$("#form-submit").prop("disabled", true);
        $("#form-submit").val("Sending...");
		hasSent = true;

        console.log("for submitted")
        console.log("name: " + name)
        console.log("email: " + email)
        console.group("message: " + message)

        fetch("https://api.cowboycocktails3.com/message", 
            {
                method: "POST", 
                body: JSON.stringify({name: name, email: email, message: message}),
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json',
                }
            }
        ).then(response => response.json())
        .then(data => {
            $("#form-submit").val("Message Sent!");
        })
        .catch((err) => {
            $("#form-submit").val("Error");
        });

		// var settings = {
		// 	"async": true,
		// 	"crossDomain": true,
		// 	"url": "https://0r1iymyyel.execute-api.us-west-2.amazonaws.com/v1/contact",
		// 	"method": "POST",
		// 	"headers": {
		// 		"content-type": "application/json"
		// 	},
		// 	"processData": false,
		// 	"data": JSON.stringify({"name": name, "email": email, "message": body})
		// }

		// $.ajax(settings).done(function (response) {
		// 	if(response.emailSent == true) {
		// 		$('#submit_button').text("Sent ✓");
		// 	}
		// 	else {
		// 		$('#submit_button').css('color', 'red').css('border-color', 'red').text("Sending Failed ✘");
		// 	}
		// });
	});

    $('#form-reset').click(function(e) {
		e.preventDefault()
		$("#form-submit").prop("disabled", false);
        $("#name").val("");
		$('#email').val("");
		$('#message').val("");
        $("#form-submit").val("Send Message");
	});
});