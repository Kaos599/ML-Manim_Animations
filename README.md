# ML-Manim Animations

This repository aims to explain and animate complex Machine Learning research papers using [Manim Community Edition](https://www.manim.community/). The goal is to make advanced ML concepts more accessible and understandable through high-quality visual explanations.

## Papers & Animations

| Research Paper Name                                            | Paper PDF Link                             | Animation Link                                 | Additional Resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------|--------------------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | [PDF](https://arxiv.org/pdf/1810.04805) | [BERT Breakthrough](BERT/media/videos/1080p60/BERTBreakthrough.mp4) | - [BERT Explained: A Complete Guide to Understanding BERT](https://towardsdatascience.com/bert-explained-a-complete-guide-with-theory-and-code-implementation-f6153b81177b)<br/>- [The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning)](https://jalammar.github.io/illustrated-bert/)<br/>- [Hugging Face Transformers Library (BERT)](https://huggingface.co/docs/transformers/model_doc/bert) |
| Improving Language Understanding by Generative Pre-training | [PDF](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | [GPT Animation](GPT/media/videos/1080p60/gpt_paper_animation_720p.mp4) | - [The Illustrated GPT-2 (Visualizing Transformer Language Models)](https://jalammar.github.io/illustrated-gpt2/)<br/>- [Hugging Face Transformers Library (GPT)](https://huggingface.co/docs/transformers/model_doc/gpt) |

## How to Use This Repo

Each animation is typically contained within its own directory (e.g., `BERT/`).

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/ML-Manim_Animations.git
    cd ML-Manim_Animations
    ```

2.  **Install ManimCE:**
    If you haven't already, install Manim Community Edition. It's highly recommended to use a virtual environment.
    ```bash
    pip install manim
    ```
    For more detailed installation instructions, refer to the [ManimCE Documentation](https://www.manim.community/en/stable/installation.html).

3.  **Run an Animation:**
    Navigate to the directory of the animation you want to render and run the `main.py` script.
    For example, to render the BERT animation:
    ```bash
    cd BERT
    manim -pql main.py BERTBreakthrough
    ```
    Or to render the GPT animation:
    ```bash
    cd GPT
    manim -pql main.py GPTPaperAnimation
    ```
    *   `-p`: Plays the animation after rendering.
    *   `-q l`: Renders in low quality (for quick previews). Use `-q h` for high quality (1080p) or `-q k` for 4K.
    *   `-l`: Leaves the progress bars (if configured in `main.py`).

    The rendered video will be saved in `BERT/media/videos/1080p60/` (or similar, depending on quality settings).

## Contributing

Contributions are welcome! If you'd like to contribute an animation for a research paper:

1.  Fork the repository.
2.  Create a new directory for your paper (e.g., `YourPaperName/`).
3.  Add your Manim Python script (`main.py`) and any necessary media files.
4.  Update the `README.md` with an entry for your new paper and animation.
5.  Submit a Pull Request.

Please ensure your animations are clear, accurate, and well-commented.

## License

This project is open-sourced under the MIT license. See the [LICENSE](LICENSE) file for details. 
