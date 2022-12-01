
$(document).ready(function()
{
  $("#selected_parameter").change(function(){

      debugger
      let parameter=$(this).val();

      // clearBtn.setAttribute("usrOn", "1")
      var hiddenElement = document.getElementById("user_email");
      hiddenElement.setAttribute("value", parameter) 

  })
}
)
