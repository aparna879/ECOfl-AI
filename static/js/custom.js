$(document).ready(function(){
    var show_btn=$('.show-modal');
    var show_btn=$('.show-modal');
    //$("#testmodal").modal('show');
    
      show_btn.click(function(){
        $("#testmodal").modal('show');
    })
  });
  
  $(function() {
          $('#element').on('click', function( e ) {
              Custombox.open({
                  target: '#testmodal-1',
                  effect: 'fadein'
              });
              e.preventDefault();
          });
      });