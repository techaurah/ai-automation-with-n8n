# Lesson 25: RAG in n8n: answers from your documents, with sources

**Time:** about 75 minutes · **Difficulty:** Intermediate · **Prerequisites:** Lessons 20, 21, 22 · **You need:** Your instance, Ollama with a chat model and an embeddings model (named in the workflows) for the live path. The twin is pure stdlib.

Retrieval-augmented generation is how an agent answers from *your* documents instead of its training: load the documents, split them into chunks, embed the chunks into a vector store, and at question time retrieve the relevant chunks and let the model answer from them, with citations. n8n expresses the whole pipeline as nodes, and this lesson builds both halves: the loading workflow that fills the store, and the asking workflow whose agent uses the store as a tool. Course 1 built RAG from scratch in Python; here the same ideas wear nodes, and the twin keeps the mechanics honest.

## The loading pipeline: load, split, embed, store

Workflow 25a is the pipeline in canvas form. The **Default Data Loader** turns incoming items into documents (in real projects it also reads files, web pages, and app data through sibling loaders). The **Recursive Character Text Splitter** cuts documents into chunks (this lesson: 500 characters with 50 of overlap, so a sentence straddling a cut survives in both neighbours; chunking choices are retrieval quality choices, and Course 1 Lesson 18's reasoning applies verbatim). The **embeddings model** (Ollama's `nomic-embed-text` here, or a hosted embeddings node) converts each chunk into a vector, a list of numbers capturing meaning. The **In Memory Vector Store** in insert mode holds them under a memory key.

Two production truths ride along. The in-memory store forgets everything when the instance restarts, which is fine for a lesson and a demo, and a data-loss incident for a business: graduate to a persistent vector store node (Qdrant, Pinecone, Supabase, or Postgres with pgvector) when the knowledge matters, exactly the Simple Memory graduation pattern from Lesson 23. And loading is a batch job with versions: when the price list changes, the store must be reloaded or updated, and the workflow that does it should be as engineered as any other in this course (scheduled, logged, idempotent by document key).

## The asking half: retrieval as a tool

Workflow 25b gives the agent a **Vector Store Tool** backed by the same store in retrieve mode: the agent decides a factual question needs the clinic's documents, the tool embeds the question with the same embeddings model (this must match the loading side, or the vectors live in different spaces and retrieval is nonsense), fetches the top chunks, and the model answers from them. The system message carries the RAG discipline: answer from the retrieved text, **name the source document**, and abstain when retrieval returns nothing relevant. An alternative shape, the dedicated question-answering chain, retrieves once and answers without agent tool-choice; prefer it when every question needs the documents, and prefer the tool shape when the agent has other tools and only some questions are document questions.

The twin is the same pipeline with counting instead of embeddings: term-overlap ranking over sentence chunks, extractive answers with the source named, and an abstention when the score is zero. It will not beat real embeddings on paraphrase (ask it about "cleaning" and it misses the hygiene chunk, a failure worth causing deliberately in the exercise), and that gap is the honest advertisement for what embeddings buy.

## Evaluation, briefly and necessarily

RAG quality fails in three places and each has a test: **retrieval** (does the right chunk come back? test with question and expected-source pairs, no model involved), **grounding** (does the answer stay inside the retrieved text? test by asking about facts adjacent to, but absent from, the documents), and **abstention** (does it decline when retrieval is empty? the payment-plan question is the standing test in both twin and workflow). Ten question pairs, run after every change to documents, chunking, or models, is a real eval harness for a system this size, and it is the difference between tuning RAG and merely having RAG.

## Run it

Run the twin (`python3 rag_twin.py`): two grounded answers with sources, one abstention. Then run workflow 25a to load the store, then publish and chat with 25b: ask the whitening price, the emergency days, and the payment-plan question. In the 25b execution, open the vector store tool's output and read the retrieved chunks yourself; the answer should use them and name prices.txt. Ask the cleaning question ("how much for a cleaning?") and watch semantic retrieval find the hygiene chunk that the twin's counting missed; that moment is the embeddings dividend, visible.

## Common failures

- **Mismatched embeddings models.** Loading with one embeddings model and asking with another retrieves garbage confidently. One model per store, named in both workflows, changed only with a full reload.
- **The store that forgets.** In-memory storage plus an instance restart equals an agent that suddenly knows nothing, with no error anywhere. Persistent store for anything a business relies on.
- **Chunks like gravel or boulders.** Tiny chunks lose context, huge chunks dilute relevance and cost tokens. Start near the lesson's sizes and tune with the question pairs, not by feel.
- **Answers without sources.** A RAG answer a human cannot check is a chatbot answer with extra infrastructure. The citation is the feature; the system message must demand it.

## Recap checklist

- [ ] I can build the load pipeline: loader, splitter, embeddings, store, in the right order.
- [ ] My agent retrieves before answering factual questions and cites the source document.
- [ ] I know the in-memory store's limit and my graduation path to a persistent one.
- [ ] I hold a small question-pair set and run it after RAG changes.

## Resources

- [n8n: RAG in n8n documentation](https://docs.n8n.io/advanced-ai/rag/)
- [n8n: vector store nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstore/)
- [Agentic AI for Beginners, Lessons 18 to 20 (RAG from scratch)](https://github.com/techaurah/agentic-ai-for-beginners)
- [n8n documentation home](https://docs.n8n.io/)
