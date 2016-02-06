$(document).ready(function() {
    $("#departing").datepicker();
    $("button").click(function() {
    	var selected = $("#dropdown option:selected").text();
        var departing = $("#departing").val();
        if (departing === "") {
			alert("Please select departing dates.");
        } else {
			confirm("Would you like to go to " + selected + " on " + departing + "?");
        }
    });
});