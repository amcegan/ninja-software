(function ($) {
	$(document).ready(function () {

		// Scroll to Top
		jQuery('.scrolltotop').click(function () {
			jQuery('html').animate({ 'scrollTop': '0px' }, 400);
			return false;
		});

		jQuery(window).scroll(function () {
			var upto = jQuery(window).scrollTop();
			if (upto > 500) {
				jQuery('.scrolltotop').fadeIn();
			} else {
				jQuery('.scrolltotop').fadeOut();
			}
		});


		$('.menu-item ul li a').click(function () {
			$('.menu-item ul li a').removeClass("active");
			$(this).addClass("active");
		});

		$('.mobile-menu-item ul li a').click(function () {
			$('.mobile-menu-item ul li a').removeClass("m-active");
			$(this).addClass("m-active");
		});

		if ($.fn.owlCarousel && $("#owl-csel1").length) {
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
			responsive: {
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
		}

		function initTestimonialCarousel() {
			if (!$.fn.owlCarousel || !$("#owl-csel2").length) { return; }
			$("#owl-csel2").owlCarousel({
				items: 3,
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
				responsive: {
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
			var script = document.createElement('script');
			script.src = 'js/testimonials.js';
			script.onload = function () {
				$('#testimonial-container').html(testimonialHTML);
				initTestimonialCarousel();
			};
			document.head.appendChild(script);
		} else if ($('#owl-csel2').length) {
			initTestimonialCarousel();
		}









	});
})(jQuery);

AOS.init({
	duration: 1000,
	once: true
})
