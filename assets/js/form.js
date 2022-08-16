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
	});

    $('#form-reset').click(function(e) {
		e.preventDefault()
		$("#form-submit").prop("disabled", false);
        $("#name").val("");
		$('#email').val("");
		$('#message').val("");
        $("#form-submit").val("Send Message");
	});

    $("#name").focus(function() {
        fetch("https://api.cowboycocktails3.com/warmup", 
            {
                method: "GET", 
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json',
                }
            }
        ).then(response => response.json())
    });
});