# To run this, you need ManimCE installed: pip install manim
# Then, simply execute from your terminal: python this_script_name.py

from manim import *

class ManimBrain(VGroup):
    """A custom VGroup that creates a stylized brain icon."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        outline = Ellipse(width=1.0, height=0.8, color=ORANGE).scale(0.8)
        midline = Line(outline.get_top(), outline.get_bottom(), stroke_width=2)
        left_fold1 = Arc(radius=0.2, start_angle=PI/2, angle=PI, stroke_width=2).move_to(outline.get_center() + LEFT*0.2 + UP*0.1)
        left_fold2 = Arc(radius=0.15, start_angle=PI*1.5, angle=-PI, stroke_width=2).move_to(outline.get_center() + LEFT*0.25 + DOWN*0.15)
        right_fold1 = Arc(radius=0.2, start_angle=PI/2, angle=-PI, stroke_width=2).move_to(outline.get_center() + RIGHT*0.2 + UP*0.1)
        right_fold2 = Arc(radius=0.15, start_angle=-PI/2, angle=PI, stroke_width=2).move_to(outline.get_center() + RIGHT*0.25 + DOWN*0.15)
        self.add(outline, midline, left_fold1, left_fold2, right_fold1, right_fold2)
        self.move_to(ORIGIN)

class BERTBreakthrough(Scene):
    """A visually enhanced animation explaining the core concepts of BERT."""
    def construct(self):
        self.show_title_screen()
        self.show_unidirectional_problem()
        self.show_bert_architecture()
        self.show_masked_language_model()
        self.show_next_sentence_prediction()
        self.show_fine_tuning_power()
        self.show_final_synthesis()

    def show_title_screen(self):
        # Add "Let's Understand" above BERT
        lets_understand = Text("Let's Understand", font_size=48, color=WHITE).move_to(UP*1.5)
        title = Text("BERT", font_size=120, weight=BOLD).set_color_by_gradient(BLUE_C, PURPLE_B)
        full_form = Text("Bidirectional Encoder Representations from Transformers", font_size=32).next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(lets_understand, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(title, shift=UP))
        self.wait(0.5)
        self.play(Write(full_form))
        self.wait(3)
        self.play(FadeOut(lets_understand, title, full_form, shift=DOWN))
        self.wait(0.5)

    def show_unidirectional_problem(self):
        title = Text("The Old Way: A One-Way Street", font_size=36).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Create properly aligned sentence
        words = ["The", "model", "finished", "its", "____"]
        word_objects = []
        
        # Create first word
        first_word = Text(words[0], font_size=32)
        word_objects.append(first_word)
        
        # Position subsequent words with consistent spacing
        for i in range(1, len(words)):
            word = Text(words[i], font_size=32)
            word.next_to(word_objects[-1], RIGHT, buff=0.3)
            word_objects.append(word)
        
        # Center the entire sentence group
        sentence_group = VGroup(*word_objects)
        sentence_group.move_to(ORIGIN + UP*0.5)
        
        # Highlight the model
        word_objects[1].set_color(BLUE)
        
        self.play(LaggedStart(*[FadeIn(word, shift=DOWN) for word in word_objects], lag_ratio=0.2))
        self.wait(1)

        # Create arrows that curve UPWARD from words to target
        target = word_objects[4]
        arrow_group = VGroup()
        
        for i in range(4):
            start_point = word_objects[i].get_top() + UP*0.1
            end_point = target.get_top() + UP*0.1
            
            # Create curved arrow that arcs upward
            arrow = CurvedArrow(
                start_point, 
                end_point, 
                angle=-PI/3,  # Negative angle for upward curve
                color=BLUE_D, 
                stroke_width=3,
                tip_length=0.2
            )
            arrow_group.add(arrow)
        
        self.play(LaggedStart(*[Create(a) for a in arrow_group], lag_ratio=0.15))

        caption = Text("Models could only use past context to predict the future.", font_size=24).next_to(sentence_group, DOWN, buff=1.5)
        self.play(Write(caption))
        
        # Show prediction possibilities
        possibilities = VGroup(
            Text("training?", color=RED_C, font_size=20), 
            Text("report?", color=RED_C, font_size=20), 
            Text("lunch?", color=RED_C, font_size=20)
        ).arrange(DOWN, buff=0.2).next_to(target, RIGHT, buff=0.8)
        
        self.play(LaggedStart(*[FadeIn(p, shift=LEFT) for p in possibilities], lag_ratio=0.3))

        self.wait(3)
        self.play(FadeOut(title, sentence_group, arrow_group, caption, possibilities))
        self.wait(0.5)

    def show_bert_architecture(self):
        title = Text("BERT's Revolutionary Architecture", font_size=36).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Create transformer layers visualization
        layers = VGroup()
        for i in range(3):
            layer = Rectangle(width=6, height=0.8, color=BLUE_B, fill_opacity=0.3)
            layer_text = Text(f"Transformer Layer {i+1}", font_size=18).move_to(layer)
            layer_group = VGroup(layer, layer_text)
            layers.add(layer_group)
        
        layers.arrange(UP, buff=0.3).move_to(ORIGIN)
        
        # Add bidirectional arrows
        bidirectional_arrows = VGroup()
        for i in range(len(layers)-1):
            up_arrow = Arrow(layers[i].get_top(), layers[i+1].get_bottom(), color=GREEN, stroke_width=3)
            down_arrow = Arrow(layers[i+1].get_bottom(), layers[i].get_top(), color=GREEN, stroke_width=3)
            bidirectional_arrows.add(up_arrow, down_arrow)
        
        self.play(LaggedStart(*[FadeIn(layer, shift=UP) for layer in layers], lag_ratio=0.3))
        self.play(LaggedStart(*[Create(arrow) for arrow in bidirectional_arrows], lag_ratio=0.1))
        
        caption = Text("Each layer can see information from ALL directions", font_size=24, color=GREEN).next_to(layers, DOWN, buff=0.8)
        self.play(Write(caption))
        
        self.wait(2)
        self.play(FadeOut(title, layers, bidirectional_arrows, caption))

    def show_masked_language_model(self):
        title = Text("BERT's Masked Language Model", font_size=36).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Create a properly aligned sentence that fits the screen
        words_text = ["The", "model", "was", "trained", "on", "large", "datasets"]
        
        # Create word objects with consistent positioning
        word_objects = []
        first_word = Text(words_text[0], font_size=28)
        word_objects.append(first_word)
        
        for i in range(1, len(words_text)):
            word = Text(words_text[i], font_size=28)
            word.next_to(word_objects[-1], RIGHT, buff=0.25)
            word_objects.append(word)
        
        # Center the sentence and ensure it fits
        sentence_group = VGroup(*word_objects)
        sentence_group.move_to(ORIGIN + UP*1)
        
        self.play(LaggedStart(*[Write(word) for word in word_objects], lag_ratio=0.1))
        self.wait(1)

        caption1 = Text("BERT randomly masks words during training", font_size=24).next_to(sentence_group, DOWN, buff=1.2)
        self.play(Write(caption1))

        # Mask the word "large" (index 5)
        target_word = word_objects[5]  # "large"
        original_text = target_word.text
        mask_token = Text("[MASK]", color=YELLOW, weight=BOLD, font_size=22)
        mask_token.match_height(target_word)  # Ensures same height as original word
        mask_token.move_to(target_word.get_center())
        
        # Add glowing effect
        mask_glow = SurroundingRectangle(
            mask_token, 
            color=YELLOW, 
            buff=0.15, 
            corner_radius=0.1, 
            fill_opacity=0.3,
            stroke_width=2
        )
        
        self.play(
            FadeOut(target_word),
            FadeIn(mask_token),
            Create(mask_glow)
        )
        self.wait(1)
        
        caption2 = Text("It uses BOTH left and right context to predict the masked word", font_size=24).next_to(sentence_group, DOWN, buff=1.2)
        self.play(Transform(caption1, caption2))

        # Create bidirectional context arrows that arc properly above the text
        left_context = word_objects[4]  # "on"
        right_context = word_objects[6]  # "datasets"
        
        # Calculate arc points above the sentence
        arc_height = 1.5
        left_arc_start = left_context.get_center() + UP*0.3
        right_arc_start = right_context.get_center() + UP*0.3
        mask_center = mask_token.get_center() + UP*0.3
        
        # Create smooth curved arrows
        left_arrow = CurvedArrow(
            left_arc_start,
            mask_center,
            angle=-PI/2,
            color=GREEN,
            stroke_width=4,
            tip_length=0.25
        )
        
        right_arrow = CurvedArrow(
            right_arc_start,
            mask_center,
            angle=PI/2,
            color=GREEN,
            stroke_width=4,
            tip_length=0.25
        )
        
        self.play(Create(left_arrow), Create(right_arrow))
        
        # Show prediction process
        prediction_text = Text("Prediction: 'large'", color=GREEN, font_size=20).next_to(mask_token, UP, buff=0.8)
        self.play(Write(prediction_text))
        
        # Reveal the correct word
        predicted_word = Text(original_text, color=GREEN, weight=BOLD, font_size=28)
        predicted_word.match_height(target_word)
        predicted_word.move_to(mask_token.get_center())
        
        self.play(
            FadeOut(mask_glow),
            Transform(mask_token, predicted_word),
            FadeOut(left_arrow, right_arrow),
            FadeOut(prediction_text)
        )
        
        self.wait(2)
        self.play(FadeOut(title, sentence_group, mask_token, caption1))
        self.wait(0.5)

    def show_next_sentence_prediction(self):
        title = Text("Next Sentence Prediction Task", font_size=36).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Create CLS token with brain - positioned higher to avoid overlap
        brain_cls = VGroup(
            ManimBrain().scale(0.4), 
            Text("[CLS]", weight=BOLD, font_size=16).next_to(ManimBrain().scale(0.4), DOWN, buff=0.1)
        ).move_to(UP*2.5)
        
        self.play(FadeIn(brain_cls))
        
        # Create sentence blocks with better spacing
        def create_sentence_block(text, color, width=8):
            text_mobj = Text(text, font_size=20)
            # Ensure text fits within specified width
            if text_mobj.width > width - 0.8:
                text_mobj.scale((width - 0.8) / text_mobj.width)
            
            box = RoundedRectangle(
                height=text_mobj.height + 0.6, 
                width=width, 
                corner_radius=0.2, 
                color=color, 
                fill_opacity=0.4,
                stroke_width=2
            )
            text_mobj.move_to(box.get_center())
            return VGroup(box, text_mobj)

        # First example - coherent sentences
        sentence_a1 = create_sentence_block("Machine learning transforms industries", BLUE_C)
        sentence_b1 = create_sentence_block("It enables automated decision making", TEAL_C)
        
        sentence_a1.move_to(UP*0.8)
        sentence_b1.move_to(DOWN*0.2)
        
        self.play(FadeIn(sentence_a1, shift=LEFT))
        self.play(FadeIn(sentence_b1, shift=RIGHT))
        
        # Clear connection lines to CLS token
        line_a1 = Line(sentence_a1.get_top(), brain_cls.get_bottom(), color=ORANGE, stroke_width=3)
        line_b1 = Line(sentence_b1.get_top(), brain_cls.get_bottom(), color=ORANGE, stroke_width=3)
        
        self.play(Create(line_a1), Create(line_b1))
        
        # Show prediction
        verdict_box = RoundedRectangle(width=2, height=0.8, color=GREEN, fill_opacity=0.6)
        verdict_text = Text("IsNext", color=WHITE, weight=BOLD, font_size=18).move_to(verdict_box)
        verdict_group = VGroup(verdict_box, verdict_text).next_to(brain_cls, RIGHT, buff=1)
        
        self.play(FadeIn(verdict_group))
        self.wait(1.5)
        
        # Second example - incoherent sentences
        sentence_b2 = create_sentence_block("Pizza tastes better with extra cheese", RED_C)
        sentence_b2.move_to(sentence_b1.get_center())
        
        self.play(Transform(sentence_b1, sentence_b2))
        
        # Update connection line
        line_b2 = Line(sentence_b1.get_top(), brain_cls.get_bottom(), color=ORANGE, stroke_width=3)
        self.play(Transform(line_b1, line_b2))
        
        # Show new prediction
        verdict_box2 = RoundedRectangle(width=2.5, height=0.8, color=RED, fill_opacity=0.6)
        verdict_text2 = Text("NotNext", color=WHITE, weight=BOLD, font_size=18).move_to(verdict_box2)
        verdict_group2 = VGroup(verdict_box2, verdict_text2).move_to(verdict_group.get_center())
        
        self.play(Transform(verdict_group, verdict_group2))
        
        # Add explanation
        explanation = Text("BERT learns to understand sentence relationships", font_size=22, color=GRAY).next_to(sentence_b1, DOWN, buff=1)
        self.play(Write(explanation))
        
        self.wait(3)
        self.play(FadeOut(title, sentence_a1, sentence_b1, brain_cls, line_a1, line_b1, verdict_group, explanation))
        self.wait(0.5)


    def show_fine_tuning_power(self):
        title = Text("BERT's Fine-tuning Versatility", font_size=36).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Create BERT base model
        bert_base = RoundedRectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3)
        bert_text = Text("Pre-trained\nBERT", font_size=18, weight=BOLD).move_to(bert_base)
        bert_model = VGroup(bert_base, bert_text).move_to(LEFT*3)
        
        self.play(FadeIn(bert_model))
        
        # Create different task heads
        tasks = [
            ("Question\nAnswering", GREEN),
            ("Sentiment\nAnalysis", ORANGE),
            ("Named Entity\nRecognition", PURPLE),
            ("Text\nClassification", RED)
        ]
        
        task_heads = VGroup()
        for i, (task_name, color) in enumerate(tasks):
            task_box = RoundedRectangle(width=2, height=1, color=color, fill_opacity=0.3)
            task_text = Text(task_name, font_size=14).move_to(task_box)
            task_head = VGroup(task_box, task_text)
            task_heads.add(task_head)
        
        task_heads.arrange_in_grid(2, 2, buff=0.5).move_to(RIGHT*2.5)
        
        # Create arrows from BERT to each task
        arrows = VGroup()
        for task_head in task_heads:
            arrow = Arrow(bert_model.get_right(), task_head.get_left(), color=GRAY, stroke_width=3)
            arrows.add(arrow)
        
        self.play(LaggedStart(*[FadeIn(task_head) for task_head in task_heads], lag_ratio=0.2))
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.1))
        
        explanation = Text("One pre-trained model → Multiple specialized applications", font_size=22).next_to(task_heads, DOWN, buff=1)
        self.play(Write(explanation))
        
        self.wait(3)
        self.play(FadeOut(title, bert_model, task_heads, arrows, explanation))

    def show_final_synthesis(self):
        final_title = Text("The BERT Revolution", font_size=48, weight=BOLD).to_edge(UP, buff=0.5)
        
        # Create key concepts with icons
        concepts = VGroup()
        
        # Bidirectional concept
        bi_icon = DoubleArrow(LEFT, RIGHT, color=GREEN, stroke_width=4)
        bi_text = Text("Bidirectional\nContext", font_size=18).next_to(bi_icon, DOWN, buff=0.2)
        bi_concept = VGroup(bi_icon, bi_text)
        
        # Masking concept
        mask_icon = Text("[MASK]", color=YELLOW, weight=BOLD, font_size=20)
        mask_text = Text("Masked Language\nModeling", font_size=18).next_to(mask_icon, DOWN, buff=0.2)
        mask_concept = VGroup(mask_icon, mask_text)
        
        # NSP concept
        nsp_icon = VGroup(
            Text("A", font_size=16, color=BLUE),
            Arrow(ORIGIN, RIGHT*0.5, stroke_width=3),
            Text("B", font_size=16, color=BLUE).shift(RIGHT*0.7)
        )
        nsp_text = Text("Next Sentence\nPrediction", font_size=18).next_to(nsp_icon, DOWN, buff=0.2)
        nsp_concept = VGroup(nsp_icon, nsp_text)
        
        concepts.add(bi_concept, mask_concept, nsp_concept)
        concepts.arrange(RIGHT, buff=1.5).move_to(ORIGIN)
        
        # Add footer early so it's visible throughout
        footer = Text("Animation by: Harsh Dayal", font_size=24, color=GRAY)
        footer.to_edge(DOWN, buff=0.3)
        
        self.play(Write(final_title))
        self.play(FadeIn(footer))  # Show footer early
        self.play(LaggedStart(*[FadeIn(concept, shift=UP) for concept in concepts], lag_ratio=0.3))
        
        # Final BERT logo
        final_logo = Text("BERT", font_size=120, weight=BOLD).set_color_by_gradient(BLUE_C, PURPLE_B)
        final_caption = Text("Transforming Natural Language Understanding", slant=ITALIC, font_size=24).next_to(final_logo, DOWN, buff=0.4)
        final_group = VGroup(final_logo, final_caption)
        
        self.wait(2)
        self.play(
            Transform(concepts, final_group),
            FadeOut(final_title),
            run_time=3
        )
        self.wait(4)  

if __name__ == "__main__":
    # The following config settings are for local rendering.
    config.pixel_height = 720
    config.pixel_width = 1280
    config.frame_rate = 30
    config.leave_progress_bars = True
    config.output_file = "BERT_Enhanced_Animation"
    
    scene = BERTBreakthrough()
    scene.render()