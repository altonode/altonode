$(function() {

  $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
    preventSubmit: true,
    submitError: function($form, event, errors) {
      // additional error messages or events
    },
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // get values from FORM
      var name = $("input#name").val();
	  var endpoint = $('#contactForm').attr('action')
      var firstName = name; // For Success/Failure Message
      // Check for white space in name for Success/Fail message
      if (firstName.indexOf(' ') >= 0) {
        firstName = name.split(' ').slice(0, -1).join(' ');
      }
	  $this = $("#sendMessageButton");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: endpoint,
        type: "POST",
        data: $form.serialize(),
        cache: false,
        success: function(data) {
          // Success message
          $('#success').html("<div class='alert alert-success'>");
          $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-success').append($("<strong>").text("Subscription successful " + firstName + ", our team will contact you with further details!" ));
          $('#success > .alert-success').append('</strong>');
          $('#success > .alert-success').append('</div>');
          //clear all fields
          $('#contactForm').trigger("reset");
        },
        error: function(data) {
		  // Fail message
          $('#success').html("<div class='alert alert-danger'>");
          $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
		  .append("</button>");
          $('#success > .alert-danger').append($("<strong>").text("Please try again " + firstName ));
          $('#success > .alert-danger').append('</strong>');
          $('#success > .alert-danger').append('</div>');
          //process validation errors here.
		  var errors = data.responseJSON; //this will get the errors response data.
		  //show them somewhere in the markup
		  //e.g
		  $.each( errors, function( field, values ) {
			  var errorsLength = values.length;
			  errorList = ""
			  for (var i = 0; i < errorsLength; i++){
				  errorList += "<li>" + values[i] + "</li>"
			  }
			  errors_markup = "<ul role=\"alert\">" + errorList + "</ul>";
			  console.log(errors_markup)
			  $("p#" + field ).append( errors_markup );
		  });
        },
        complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });

  $("a[data-toggle=\"tab\"]").click(function(e) {
    e.preventDefault();
    $(this).tab("show");
  });
});

/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
  $('#success').html('');
});
