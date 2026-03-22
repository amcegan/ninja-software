(function($){
	$(document).ready(function() {	

		// Scroll to Top
		jQuery('.scrolltotop').click(function(){
			jQuery('html').animate({'scrollTop' : '0px'}, 400);
			return false;
		});
		
		jQuery(window).scroll(function(){
			var upto = jQuery(window).scrollTop();
			if(upto > 500) {
				jQuery('.scrolltotop').fadeIn();
			} else {
				jQuery('.scrolltotop').fadeOut();
			}
		});


		$('.menu-item ul li a').click(function(){
			$('.menu-item ul li a').removeClass("active");
			$(this).addClass("active");
		});

		$('.mobile-menu-item ul li a').click(function(){
			$('.mobile-menu-item ul li a').removeClass("m-active");
			$(this).addClass("m-active");
		});

		$("#owl-csel1").owlCarousel({
					items: 4,
					autoplay: true,
					autoplayTimeout: 3000,
					startPosition: 0,
					rtl: false,
					loop: true,
					margin: 15,
					dots: false,
					nav: true,
					// center:true,
					// stagePadding: 2,
					navText: [
								'<i class="fa fa-angle-left" aria-hidden="true"></i>',
								'<i class="fa fa-angle-right" aria-hidden="true"></i>'
							],
					navContainer: '.main-content .custom-nav',
					responsive:{
						0: {
							items: 1.3,						
						},
						767: {
							items: 3,						
						},
						1200: {
							items: 5,						
						}
					}

				});

		function initTestimonialCarousel() {
			$("#owl-csel2").owlCarousel({
				items:3,
				autoplay: true,
				autoplayTimeout: 3000,
				startPosition: 0,
				rtl: false,
				loop: true,
				margin: 15,
				dots: true,
				nav: true,
				navText: [
							'<i class="fa-solid fa-arrow-left"></i>',
							'<i class="fa-solid fa-arrow-right"></i>'
						],
				navContainer: '.main-content2 .custom-nav',
				responsive:{
					0: {
						items: 1.3,						
					},
					767: {
						items: 2,						
					},
					1200: {
						items: 3,						
					}
				}
			});
		}

		if ($('#testimonial-container').length) {
			$('#testimonial-container').load('testimonials.html', function() {
				initTestimonialCarousel();
			});
		} else if ($('#owl-csel2').length) {
			initTestimonialCarousel();
		}
				
		
		
		
		
		
		
		
		
	});
})(jQuery);

AOS.init({
	duration: 1900,
})


/* ---- stats.js config ---- */

var count_particles, stats, update;
stats = new Stats;
stats.setMode(0);
stats.domElement.style.position = 'absolute';
stats.domElement.style.left = '0px';
stats.domElement.style.top = '0px';
document.body.appendChild(stats.domElement);
count_particles = document.querySelector('.js-count-particles');
update = function() {
  stats.begin();
  stats.end();
  if (window.pJSDom[0].pJS.particles && window.pJSDom[0].pJS.particles.array) {
    count_particles.innerText = window.pJSDom[0].pJS.particles.array.length;
  }
  requestAnimationFrame(update);
};
requestAnimationFrame(update);


// ===============text slider================

