import re

with open('/Users/user/projects/ninja-software/consulting.html', 'r') as f:
    content = f.read()

# Replace the specific old main content
new_html = """            <section class="document-search-section">
                <div class="document-search-container">

                    <div class="document-search-hero" >
                        <span class="document-search-eyebrow">Document Search, RAG & GraphRAG</span>
                        <h1>
                            Turn <span class="highlight-workflows">Documents into Answers</span> —
                            and Organisational Knowledge into <span class="highlight-workflows">Business Advantage</span>
                        </h1>
                        <p class="document-search-subheadline">
                            We design and build intelligent document search systems using
                            <span class="highlight-workflows">RAG</span>,
                            <span class="highlight-workflows">GraphRAG</span>, vector search, and hybrid retrieval—
                            helping your organisation find trusted answers faster, unlock hidden knowledge, and make better decisions at scale.
                        </p>
                    </div>

                    <div class="document-search-grid">

                        <div class="document-search-card" >
                            <h2>The Problem</h2>
                            <p>
                                Most organisations sit on a vast amount of valuable information, but teams still struggle to find what they need.
                            </p>
                            <ul>
                                <li>Critical knowledge is buried across <span class="highlight-workflows">documents</span>, folders, and systems</li>
                                <li>Employees waste time searching for answers or recreating work</li>
                                <li>Traditional keyword search often returns <span class="highlight-workflows">too much noise</span> and too little insight</li>
                                <li>Important relationships between documents, entities, and concepts remain hidden</li>
                            </ul>
                        </div>

                        <div class="document-search-card" >
                            <h2>Enterprise Search, Reimagined</h2>
                            <p>
                                We build modern document search platforms that go beyond simple keyword matching.
                            </p>
                            <ul>
                                <li><span class="highlight-workflows">RAG</span> to retrieve relevant content and generate grounded answers</li>
                                <li><span class="highlight-workflows">Hybrid search</span> combining keyword, semantic, and vector retrieval</li>
                                <li><span class="highlight-workflows">GraphRAG</span> to surface relationships between entities, concepts, and documents</li>
                                <li>Ranking and reranking strategies to improve relevance and trust</li>
                            </ul>
                            <p>
                                The result is a system that helps your teams find the
                                <span class="highlight-workflows">right answer</span>, not just more documents.
                            </p>
                        </div>

                        <div class="document-search-card" >
                            <h2>Built for Trust, Relevance, and Scale</h2>
                            <p>
                                For enterprise buyers, search is only valuable when it is reliable, secure, and grounded in your own data.
                            </p>
                            <ul>
                                <li>Grounded responses linked to <span class="highlight-workflows">source content</span></li>
                                <li>Search tuned for <span class="highlight-workflows">accuracy</span>, relevance, and explainability</li>
                                <li>Secure integration with your existing document stores and business systems</li>
                                <li>Architectures designed for <span class="highlight-workflows">large-scale enterprise knowledge</span></li>
                            </ul>
                            <p>
                                We engineer search systems that can be trusted in real operational environments, not just demos.
                            </p>
                        </div>

                        <div class="document-search-card" >
                            <h2>Where GraphRAG Adds Strategic Value</h2>
                            <p>
                                In many organisations, the real value is not only in individual documents, but in the
                                <span class="highlight-workflows">connections between people, topics, systems, and events</span>.
                            </p>
                            <ul>
                                <li>Reveal relationships hidden across large knowledge bases</li>
                                <li>Improve complex question answering across multiple sources</li>
                                <li>Support investigation, research, and decision-making workflows</li>
                                <li>Provide richer context than standard retrieval alone</li>
                            </ul>
                            <p>
                                GraphRAG is especially valuable where knowledge is distributed, interconnected, and difficult to navigate with standard search.
                            </p>
                        </div>

                    </div>

                    <div class="document-search-outcomes" >
                        <h2>What This Means for Your Organisation</h2>
                        <div class="document-search-outcomes-grid">
                            <div class="outcome-box">
                                <h3>Faster Access to Knowledge</h3>
                                <p>Give your teams immediate access to the information they need without digging through documents and folders.</p>
                            </div>
                            <div class="outcome-box">
                                <h3>Better Decisions</h3>
                                <p>Enable leaders and staff to act on accurate, grounded answers drawn from trusted internal knowledge.</p>
                            </div>
                            <div class="outcome-box">
                                <h3>Higher Productivity</h3>
                                <p>Reduce time wasted searching, repeating research, or relying on tribal knowledge.</p>
                            </div>
                            <div class="outcome-box">
                                <h3>Scalable Knowledge Infrastructure</h3>
                                <p>Turn fragmented document collections into a searchable, reusable knowledge system that grows with your business.</p>
                            </div>
                        </div>
                    </div>

                    <div class="document-search-use-cases" >
                        <h2>Example Use Cases</h2>
                        <div class="document-search-use-cases-grid">
                            <div class="use-case-box">
                                <h3>Enterprise Knowledge Assistants</h3>
                                <p>Help employees search policies, procedures, project documents, and internal knowledge with natural language.</p>
                            </div>
                            <div class="use-case-box">
                                <h3>Technical & Operational Document Search</h3>
                                <p>Find answers across manuals, standards, operating procedures, and complex technical documentation.</p>
                            </div>
                            <div class="use-case-box">
                                <h3>Compliance & Risk Research</h3>
                                <p>Search contracts, policies, reports, and regulatory material with more context, precision, and traceability.</p>
                            </div>
                            <div class="use-case-box">
                                <h3>Cross-Document Investigation</h3>
                                <p>Use GraphRAG to connect entities, events, and concepts across large collections of related documents.</p>
                            </div>
                        </div>
                    </div>

                    <div class="document-search-approach" >
                        <h2>Our Approach</h2>
                        <div class="document-search-approach-grid">
                            <div class="approach-box">
                                <span class="approach-step">01</span>
                                <h3>Discovery</h3>
                                <p>We analyse your document landscape, business goals, and the questions your teams need answered.</p>
                            </div>
                            <div class="approach-box">
                                <span class="approach-step">02</span>
                                <h3>Retrieval Design</h3>
                                <p>We design the right retrieval strategy using keyword, semantic, vector, hybrid search, and GraphRAG where appropriate.</p>
                            </div>
                            <div class="approach-box">
                                <span class="approach-step">03</span>
                                <h3>Grounded Answering</h3>
                                <p>We build systems that generate answers grounded in your source documents, with traceability and trust built in.</p>
                            </div>
                            <div class="approach-box">
                                <span class="approach-step">04</span>
                                <h3>Production Deployment</h3>
                                <p>We integrate the solution into your environment securely and tune it for relevance, performance, and adoption.</p>
                            </div>
                        </div>
                    </div>

                    <div class="document-search-cta" >
                        <h2>Unlock the Value Hidden in Your Documents</h2>
                        <p>
                            Move beyond basic search and build a document intelligence platform that helps your organisation find answers faster, work smarter, and make better decisions.
                        </p>
                        <div class="document-search-cta-buttons">
                            <a href="#contact" class="btn-primary">Book a Consultation</a>
                            <a href="#contact" class="btn-secondary">Discuss Your Document Search Use Case</a>
                        </div>
                    </div>

                </div>
            </section>"""

# Find the block between `<main>` and `<!-- footer start -->` and replace it
import re

pattern = re.compile(r'(<main>.*?)<!-- pagination page start.*?<!-- contact-form-area  end -->', re.DOTALL)
content = pattern.sub(r'\1' + new_html, content)

with open('/Users/user/projects/ninja-software/consulting.html', 'w') as f:
    f.write(content)

