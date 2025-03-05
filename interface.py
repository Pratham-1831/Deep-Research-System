import streamlit as st
from workflows.research_workflow import ResearchWorkflow
from utils.logger import log
import time

def main():
    st.set_page_config(
        page_title="Deep Research AI",
        page_icon="🔍",
        layout="centered"
    )

    st.markdown(
        """
        <style>
        .report-title { font-size: 2.5rem; color: #1f77b4; }
        .sidebar .sidebar-content { background-color: #f0f2f6; }
        .stProgress > div > div > div { background-color: #1f77b4; }
        </style>
        """, unsafe_allow_html=True
    )

    # Sidebar input
    with st.sidebar:
        st.title("Configuration")
        query=st.text_input("Research Query",placeholder="Enter your research question...")
        st.caption("Example: 'Evolution of AI over the years'")

    # Main title
    st.markdown("<h1 class='report-title'>Deep Research AI</h1>",unsafe_allow_html=True)

    if query:
        with st.status("🔍Conducting Research...",expanded=True) as status:
            workflow=ResearchWorkflow()

            # Phase 1: Web search
            st.write("### Phase 1: Web Search")
            research_progress = st.progress(0, text="Gathering sources...")
            start_time=time.time()

            try:
                results=workflow.graph.invoke({"query":query})

                research_progress.progress(100,"Research complete!")
                st.success(f"Found {len(results['search_results'])}relevant sources")

                # Phase 2: Analysis & Synthesis
                st.write("### Phase 2: Analysis & Synthesis")
                analysis_progress=st.progress(0,text="Processing content...")

                time.sleep(1)
                analysis_progress.progress(100,"Analysis Complete!")

                status.update(label="Research Complete!",state="complete",expanded=False)

                # Research Report
                st.markdown("----")
                st.subheader("Research Report")
                st.markdown(results["answer"])

            except Exception as e:
                log.error(f"Research failed:{str(e)}")
                status.update(label="Research Failed",state="error")  
                st.error(f"Research failed:{str(e)}")

        
        st.markdown("----")
        with st.expander("View Research Sources"):
            for i,source in enumerate(results["search_results"]):
                st.markdown(f"""
                **Source {i+1}**  
                **URL**: {source['url']}  
                **Content Preview**: {source['content'][:200]}...
                """)

        # Research Metrics
        st.markdown("----")
        col1,col2=st.columns(2)
        with col1:
            st.metric("Research Time",f"{time.time()-start_time:.1f}seconds")
        with col2:
            st.metric("Sources Analyzed",len(results["search_results"]))

if __name__ == "__main__":
    main()
