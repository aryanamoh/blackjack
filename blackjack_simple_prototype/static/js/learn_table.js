$(document).ready(function() {
    var steps = [
      { selector: '#learn-table', message: 'This is the blackjack table.' }
      // Add more steps as needed
    ];
    var currentStep = 0;
  
    $('.start-walkthrough').click(function() {
      startWalkthrough();
    });
  
    $('.next-step').click(function() {
      currentStep++;
      if (currentStep < steps.length) {
        highlightElement(steps[currentStep].selector, steps[currentStep].message);
      } else {
        endWalkthrough();
      }
    });
  
    function startWalkthrough() {
      highlightElement(steps[currentStep].selector, steps[currentStep].message);
      $('.overlay').show();
    }
  
    function endWalkthrough() {
      $('.overlay').hide();
      // You can add any final actions here after the walkthrough ends
    }
  
    function highlightElement(selector, message) {
        var element = $(selector);
        var highlight = $('.highlight');
        highlight.css({
          top: element.offset().top - $(window).scrollTop() - 5,
          left: element.offset().left - 5,
          width: element.outerWidth() + 10,
          height: element.outerHeight() + 10
        });
      
        // Calculate popup position based on highlight position and dimensions
        var popupWidth = $('.walkthrough-popup').outerWidth();
        var popupHeight = $('.walkthrough-popup').outerHeight();
        var highlightTop = highlight.offset().top;
        var highlightLeft = highlight.offset().left;
        var highlightWidth = highlight.outerWidth();
        var highlightHeight = highlight.outerHeight();

        // Adjust first popup position
        if (highlightTop == 0) {
            highlightTop = 70;
        }
        if (highlightLeft == 0) {
            highlightLeft = 10;
        }
      
        var popupTop = highlightTop + highlightHeight + 10; // Adjust as needed
        var popupLeft = highlightLeft + (highlightWidth - popupWidth) / 2; // Center horizontally
      
        $('.walkthrough-popup').css({
          top: popupTop,
          left: popupLeft
        });
      
        $('.walkthrough-popup .message').text(message);
      }
      
  });
  