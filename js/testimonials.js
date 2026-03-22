/*
When a browser opens a website via the file:// protocol (double-clicking the file), 
it applies strict security rules (CORS). The browser restricts JavaScript fetch or 
AJAX from reading other local files. Why? Because if a downloaded HTML file could 
freely read any other file on your hard drive, it would be a massive security vulnerability. 

However, browsers do allow you to load .js files via <script src="..."> tags, no matter what protocols you are using.

So, by taking the HTML and converting it into a JavaScript string inside js/testimonials.js
, we bypassed the security block. We are no longer "fetching" an HTML document; 
we are simply executing an allowed script that happens to inject HTML.

Implications of this specific change:   

HTML hidden in JavaScript: Because your HTML is now wrapped inside Javascript backticks (`), 
editing it can be slightly less convenient. Your code editor (like VS Code) might not provide 
full HTML syntax highlighting or auto-formatting inside a JavaScript string.
Syntax Sensitivity: If you ever write a testimonial that actually contains a literal 
backtick (`), you will need to "escape" it like this: ```, otherwise it will break the JavaScript file.
*/
const testimonialHTML = `
                    <div class="testimonial-wrapper">
                        <div class="main-content2">
							<div id="owl-csel2" class="owl-carousel owl-theme">
								<div>
                                    <div class="testimonial-item-box">
                                        <p>“This letter of recommendation affirms our deep gratitude for the high degree of professionalism we have experienced while working with NinjaSoftware. Our requirement for their senior programming skills and experience during multiple phases of our Digital Transformation strategy, was met with a level of expertise that has surely enabled us as a company to succeed.”</p>
                                        <div class="ts-user">
                                            <img src="img/tsuser1.png" alt="">
                                            <h4>Kim McKayed</h4>
                                            <span>Technical Director of SPIRE Intelligent Vehicle Rescue </span>
                                        </div> <!-- .ts-user -->
                                    </div> <!-- .testimonial-item-box -->
								</div>
								<div>
                                    <div class="testimonial-item-box">
                                        <p>“We had a custom-built legacy application that needed to be updated to newer technology. Anthony excelled at understanding our business requirements and implemented a solution that now forms the core of our business. I would have no hesitation in recommending Ninja Software and we will continue their services for our custom development work into the future.”</p>
                                        <div class="ts-user">
                                            <img src="img/tsuser2.png" alt="">
                                            <h4>Donal McNamee</h4>
                                            <span>Business Development Manager at Archway Products Ltd.</span>
                                        </div> <!-- .ts-user -->
                                    </div> <!-- .testimonial-item-box -->
								</div>
								<div>
                                    <div class="testimonial-item-box">
                                        <p>“We have been working with Anthony and his team at Ninja Software over the past 2 years for a complicated FinTech requirement. Initially what struck me about his approach was his attention to detail and professionalism. The end product had to be impeccable as we were dealing with large payments on monthly billing cycles. The platform has been running flawlessly since work was completed. Work done in a timely manner with excellent communication throughout. Highly recommended.”</p>
                                        <div class="ts-user">
                                            <img src="img/tsuser1.png" alt="">
                                            <h4>Kieran Walkin</h4>
                                            <span>CEO LittleVista</span>
                                        </div> <!-- .ts-user -->
                                    </div> <!-- .testimonial-item-box -->
								</div>
							</div> <!-- .owl-carousel -->
							<div class="owl-theme">
								<div class="owl-controls">
									<div class="custom-nav owl-nav"></div> <!-- .custom-nav -->
								</div> <!-- .owl-controls -->
							</div> <!-- .owl-theme -->
						</div> <!-- .main-content2 -->
                    </div> <!-- .testimonial-wrapper -->
`;
