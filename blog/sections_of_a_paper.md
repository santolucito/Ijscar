**The Structure of a Computer Science Paper**

When writing a computer science research paper, the organization of the content plays a crucial role in effectively communicating your research. Depending on whether your work is more algorithm-focused or application-oriented, the sections of your paper will vary slightly. This post walks through the common structures of both algorithmic and applied computer science papers and explain the reasoning behind these differences.

A quick note - this blog post does not address how to write a literature review. 
A literature review is a very different kind of paper than those examined here, and follows a different strucutre.
For more on this, please read our blog post of [literature review papers](/blog).

### Algorithm-Focused Papers

Algorithmic papers usually involve theoretical contributions, such as a new algorithm, a formal proof, or an optimization technique. These papers tend to follow a structure that focuses on formalization and evaluation of the method itself, often with less emphasis on external applications or user-centric evaluations.

#### Typical Structure:
1. **Abstract**  
   A concise summary of the problem, the algorithmic contribution, and the key results. See our post on [writing effective abstracts](./how_to_abstract.md).

2. **Introduction**  
   This section sets the stage by explaining the problem, its relevance, and the main contribution of the paper. In algorithmic papers, the introduction may also briefly outline the structure of the paper. End your introduction with a clear statement of the problem you are addressing and the main contributions of your work. This usually takes form of a statement like: "In summary, we make the following contributions:" followed by a bulleted list of the main contributions.

3. **Motivating Example**  
   A motivating example is often critical in algorithmic work. Since the application or use case of the algorithm might not be immediately obvious, this section illustrates why the problem is important and how the proposed method applies. The example helps ground the formalization that follows.

4. **Preliminaries**  
   Preliminaries are where you define key concepts, notations, and theorems that will be used in the formalization of the algorithm. If the reader is not familiar with certain mathematical tools or terminology, this is the place to introduce them.

5. **System Overview**  
   This section presents the high-level details of the algorithm or system before diving into the nitty-gritty. It provides the reader with an intuitive understanding of how the solution works, potentially with diagrams or flowcharts.

6. **Evaluation**  
   This is where you present the performance of your algorithm. Evaluation in algorithmic papers often involves theoretical analysis, complexity proofs, or benchmarks against known solutions to show that your contribution is effective and novel.

7. **Related Work**  
   Related work comes at the end in algorithmic papers because you want your contribution to stand on its own before comparing it to other approaches. You show how your work fits within the broader literature and justify why it advances the field.

8. **Conclusions**  
   Here, you wrap up by summarizing your contribution, highlighting the main results, and suggesting possible future directions for research.

#### Why This Structure?

In algorithmic papers, the key focus is the formal contribution. The results often speak for themselves, and the structure is designed to emphasize the novelty of the algorithm, with proofs or evaluations taking center stage. **Motivating examples** are necessary to give context, while the **related work** is usually deferred until after the main contribution so that the reader understands your algorithm independently of prior methods.

### Applied Papers (e.g., LLM Evaluations, User Studies)

Applied papers focus more on the practical implementation and evaluation of technologies. This includes works like large language model (LLM) evaluations, user studies, or system designs. These papers often have a different structure to reflect their real-world focus, emphasizing prior work, system design, and user-centric evaluations.

#### Typical Structure:
1. **Abstract**  
   A brief overview of the problem, the system or method being evaluated, and the key outcomes of the study.

2. **Introduction**  
   The introduction presents the problem, the motivation behind solving it, and a high-level view of the approach. For applied work, this also includes why the problem is practically significant, perhaps touching on societal or real-world implications. As in the algorithmic paper, often introductions will with the main contributions of your work, but this is less of a hard and fast rule in applied work.

3. **Related Work**  
   Unlike algorithmic papers, related work is often front-loaded in applied research. This is because, in applied fields, understanding the existing landscape is crucial to contextualizing the contribution. Readers need to know what has been done before and how your work builds on or diverges from existing solutions.

4. **System Overview**  
   This section describes the architecture or methodology behind your system or evaluation. For instance, in LLM evaluations, this might cover the design of experiments, the metrics used for evaluation, or how the model was fine-tuned or deployed.

5. **Evaluation**  
   Applied papers emphasize empirical evaluation. This could be through benchmarking, user studies, or performance metrics. In a user study, this section would describe the setup, participant demographics, and any statistical analysis conducted to validate the results.

6. **Discussion**  
   The discussion section is often richer in applied work. It may include interpretations of the results, discussions of limitations, or thoughts on broader implications (e.g., for real-world applications). Applied papers may also explore how results might generalize to other settings or outline unexpected challenges faced during evaluation. Often you will see a subsection here on **threats to validity** that discusses potential confounding factors or biases in the study. You may want to also read our post on [threats to validity](./threats_to_validity.md).

7. **Conclusions**  
   The conclusion summarizes your contributions, but also frequently discusses future work or implications for further studies.

#### Why This Structure?

In applied work, it’s crucial to position your contribution within the existing body of knowledge early on. This helps readers immediately understand why your system or study is significant. Moreover, the **discussion section** in applied papers often focus on broader implications, such as real-world deployment or user feedback, which makes the research more relatable. **Motivating examples** are typically less necessary since the relevance of the application is usually self-evident.

### Key Differences

- **Related Work Placement:**  
   For algorithmic papers, related work typically comes after the core contribution because you want the novelty of your method to stand on its own. In contrast, applied papers often include related work early to frame the practical importance and context of the study.
  
- **Motivating Example:**  
   Algorithmic papers frequently include motivating examples, as the application of a formal method is not always clear. Applied papers, on the other hand, rarely need this, as the problem tends to be more obvious from the start.
   
- **Discussion Section:**  
   Applied papers tend to have more to discuss in terms of user feedback, deployment challenges, or societal implications and so include a dedicated Discussion section. Algorithmic papers are often more dry in this regard so can skip this section, but recently many conferences are asking authors to include a **societal impact** section at the end in order to encourage reflection the impacts of their work beyond the computational contribution.

### Conclusion

Algorithmic and applied papers are just two categories that we have discussed here.
There are, of course, many other types of papers in computer science, that may fall slightly outside of this framework.
You can always adapt your structure as needed—just ensure it makes sense for the reader and the story you're telling.
The best resource is also to read more papers in your field to understand the common structures and conventions used in your area of research.

#### Quick tip

Don't overuse bullet points (e.g. with the enumerate environment) in your paper.
Look at papers in your field and see how the authors have organized their thoughts.
Try to emulate the structure in the papers you are citing in your paper.
An important part of writing a good paper, aside from the content itself, is making the paper ``look'' like a paper.
