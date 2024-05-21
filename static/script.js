

document.getElementById('chrisButton').addEventListener('click', function() {
    alert('Button clicked!');
});

function myFunction() {
    alert("Button clicked!");
}


$(document).ready(function(){
    $("#hideButton").click(function(){
      $("p").hide();
    });
  });

$(document).on("click", ".alert", function() {
    //alert('Button clicked!');
    bootbox.prompt({
        title: "Please enter SSID for new WiFi network:",
        callback: function(result) {
            if (result !== null) {
                // User entered a value, do something with it
                console.log("SSID entered:", result);
            } else {
                // User clicked cancel
                console.log("Prompt was canceled");
            }
        }
    });
    
});
