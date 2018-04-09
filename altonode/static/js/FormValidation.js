function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function(){
	$('#contactForm').submit(function(){
		event.preventDefault()
		var $formData = $(this).serialize()
		var $endpoint = $ajaxForm.attr("action")
		console.log($formData)
		$.ajax({
			method: "POST",
			url: $endpoint,
			data: $formData,
			success: handleFormSuccess,
			error: handleFormError,
		})	
	})
		
		function handleFormSuccess(data, textStatus, jqXHR){
			console.log(data)
			console.log(textStatus)
			console.log(jqXHR)
			$('#contactForm')[0].reset(); //reset form data
		}
		
		function handleFormError(jqXHR, textStatus, errorThrown){
			console.log(jqXHR)
			console.log(textStatus)
			console.log(errorThrown)
			$('#contactForm').find(errorThrown).show();
		}
})
