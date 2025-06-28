from manim import *
import numpy as np

# Configuration for 720p output
config.pixel_height = 720
config.pixel_width = 1280
config.frame_rate = 30

class GPTPaperAnimation(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#0f1419"
        
        # Streamlined animation focusing on key concepts
        self.title_sequence()
        self.problem_statement()
        self.core_innovation()
        self.transformer_architecture()
        self.training_process()
        self.key_results()
        self.impact_legacy()
        self.conclusion()
    
    def title_sequence(self):
        """Improved title sequence"""
        self.clear()
        
        # Main title with better spacing
        title = Text(
            "Improving Language Understanding\nby Generative Pre-Training", 
            font_size=36, 
            color=WHITE,
            line_spacing=1.3
        )
        title.move_to(UP * 1.5)
        
        # Authors with proper formatting
        authors = Text(
            "Alec Radford • Karthik Narasimhan • Tim Salimans • Ilya Sutskever", 
            font_size=22, 
            color=BLUE
        )
        authors.next_to(title, DOWN, buff=0.8)
        
        # Company and date
        openai_text = Text("OpenAI", font_size=26, color=GREEN, weight=BOLD)
        date_text = Text("June 2018", font_size=20, color=GRAY)
        
        company_date = VGroup(openai_text, date_text).arrange(DOWN, buff=0.2)
        company_date.next_to(authors, DOWN, buff=0.8)
        
        # Key message
        message = Text(
            "The Foundation of Modern Large Language Models", 
            font_size=28, 
            color=YELLOW,
            weight=BOLD
        )
        message.next_to(company_date, DOWN, buff=1.2)
        
        # Animation sequence
        self.play(FadeIn(title, shift=UP))
        self.wait(1)
        self.play(Write(authors))
        self.wait(0.8)
        self.play(FadeIn(company_date, shift=UP))
        self.wait(0.8)
        self.play(Write(message))
        self.wait(2.5)
        
        # Fade out everything
        self.play(FadeOut(VGroup(title, authors, company_date, message)))
        self.wait(0.5)
    
    def problem_statement(self):
        """Streamlined problem statement"""
        # Problem title
        problem_title = Text("The NLP Challenge in 2018", font_size=34, color=RED, weight=BOLD)
        problem_title.to_edge(UP, buff=1.2)
        
        # Core problems
        problems = [
            "Limited labeled data for specific tasks",
            "Task-specific model architectures required",
            "Poor transfer learning across different tasks",
            "Expensive manual annotation requirements"
        ]
        
        problem_list = VGroup()
        for i, problem in enumerate(problems):
            bullet = Text("•", font_size=28, color=YELLOW)
            problem_text = Text(problem, font_size=24, color=WHITE)
            
            problem_row = VGroup(bullet, problem_text)
            problem_row.arrange(RIGHT, buff=0.3)
            problem_list.add(problem_row)
        
        problem_list.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        problem_list.next_to(problem_title, DOWN, buff=1.5)
        problem_list.shift(LEFT * 0.5)
        
        # Animation
        self.play(FadeIn(problem_title, shift=DOWN))
        self.wait(1)
        
        for problem_row in problem_list:
            self.play(FadeIn(problem_row, shift=LEFT))
            self.wait(0.7)
        
        self.wait(2)
        
        # Clear for next section
        self.play(FadeOut(VGroup(problem_title, problem_list)))
        self.wait(0.5)
    
    def core_innovation(self):
        """Fixed core innovation section"""
        # Innovation title
        innovation_title = Text("GPT's Two-Stage Training Innovation", font_size=32, color=GREEN, weight=BOLD)
        innovation_title.to_edge(UP, buff=1)
        
        # Stage boxes with proper positioning for 720p
        stage1_box = Rectangle(width=4, height=2.5, color=BLUE, fill_opacity=0.1)
        stage1_box.move_to(LEFT * 2.8 + UP * 0.3)
        
        stage1_title = Text("Stage 1: Pre-training", font_size=26, color=BLUE, weight=BOLD)
        stage1_title.next_to(stage1_box.get_top(), DOWN, buff=0.3)
        
        stage1_points = VGroup(
            Text("• Unsupervised learning", font_size=18, color=WHITE),
            Text("• Large text corpus", font_size=18, color=WHITE),
            Text("• Language modeling", font_size=18, color=WHITE),
            Text("• General representations", font_size=18, color=WHITE)
        )
        stage1_points.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        stage1_points.next_to(stage1_title, DOWN, buff=0.4)
        
        stage2_box = Rectangle(width=4, height=2.5, color=YELLOW, fill_opacity=0.1)
        stage2_box.move_to(RIGHT * 2.8 + UP * 0.3)
        
        stage2_title = Text("Stage 2: Fine-tuning", font_size=26, color=YELLOW, weight=BOLD)
        stage2_title.next_to(stage2_box.get_top(), DOWN, buff=0.3)
        
        stage2_points = VGroup(
            Text("• Supervised adaptation", font_size=18, color=WHITE),
            Text("• Task-specific data", font_size=18, color=WHITE),
            Text("• Minimal architecture changes", font_size=18, color=WHITE),
            Text("• Transfer learning", font_size=18, color=WHITE)
        )
        stage2_points.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        stage2_points.next_to(stage2_title, DOWN, buff=0.4)
        
        # Improved arrow
        arrow = Arrow(
            start=stage1_box.get_right() + RIGHT * 0.1,
            end=stage2_box.get_left() + LEFT * 0.1,
            color=WHITE,
            stroke_width=5
        )
        
        # Dataset info
        dataset_info = Text("BookCorpus: 7,000+ books • Long-range dependencies", 
                           font_size=20, color=PURPLE)
        dataset_info.to_edge(DOWN, buff=1.2)
        
        # Animation sequence
        self.play(FadeIn(innovation_title, shift=DOWN))
        self.wait(1)
        
        # Stage 1
        self.play(Create(stage1_box))
        self.play(FadeIn(stage1_title, shift=DOWN))
        for point in stage1_points:
            self.play(FadeIn(point, shift=LEFT))
            self.wait(0.3)
        
        self.wait(0.5)
        
        # Arrow
        self.play(GrowArrow(arrow))
        self.wait(0.5)
        
        # Stage 2
        self.play(Create(stage2_box))
        self.play(FadeIn(stage2_title, shift=DOWN))
        for point in stage2_points:
            self.play(FadeIn(point, shift=RIGHT))
            self.wait(0.3)
        
        self.wait(1)
        self.play(FadeIn(dataset_info, shift=UP))
        self.wait(2)
        
        # Clear for next section
        all_objects = VGroup(
            innovation_title, stage1_box, stage1_title, stage1_points,
            stage2_box, stage2_title, stage2_points, arrow, dataset_info
        )
        self.play(FadeOut(all_objects))
        self.wait(0.5)
    
    def transformer_architecture(self):
        """Simplified transformer architecture for 720p"""
        # Architecture title
        arch_title = Text("GPT-1 Transformer Architecture", font_size=32, color=BLUE, weight=BOLD)
        arch_title.to_edge(UP, buff=1)
        
        # Key specifications in a clean layout
        specs_title = Text("Architecture Specifications:", font_size=26, color=YELLOW)
        specs_title.next_to(arch_title, DOWN, buff=1)
        specs_title.to_edge(LEFT, buff=1.5)
        
        specs = [
            ("Layers:", "12 decoder-only transformer layers"),
            ("Parameters:", "117 million parameters"),
            ("Hidden Size:", "768-dimensional states"),
            ("Attention Heads:", "12 multi-head attention heads"),
            ("Context Window:", "512 tokens maximum")
        ]
        
        specs_group = VGroup()
        for label, value in specs:
            label_text = Text(label, font_size=22, color=GREEN, weight=BOLD)
            value_text = Text(value, font_size=22, color=WHITE)
            
            spec_row = VGroup(label_text, value_text)
            spec_row.arrange(RIGHT, buff=0.5)
            specs_group.add(spec_row)
        
        specs_group.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        specs_group.next_to(specs_title, DOWN, buff=0.6)
        
        # Simple visual representation
        self.create_simple_transformer_visual()
        
        # Animation
        self.play(FadeIn(arch_title, shift=DOWN))
        self.wait(1)
        self.play(FadeIn(specs_title, shift=LEFT))
        self.wait(0.5)
        
        for spec in specs_group:
            self.play(FadeIn(spec, shift=LEFT))
            self.wait(0.4)
        
        self.wait(2)
        
        # Clear for next section
        self.play(FadeOut(VGroup(arch_title, specs_title, specs_group)))
        self.wait(0.5)
    
    def create_simple_transformer_visual(self):
        """Create a clean transformer visualization for 720p"""
        # Position on the right side
        base_pos = RIGHT * 3 + UP * 0.3
        
        # Input tokens
        input_text = Text("Input: \"The cat sat on\"", font_size=16, color=GREEN)
        input_text.move_to(base_pos + DOWN * 1.5)
        
        # Transformer layers (simplified)
        layers = VGroup()
        for i in range(3):
            layer = Rectangle(width=2.5, height=0.5, color=BLUE, fill_opacity=0.2)
            layer_text = Text(f"Layer {i+1}", font_size=14, color=WHITE)
            layer_group = VGroup(layer, layer_text)
            layers.add(layer_group)
        
        layers.arrange(UP, buff=0.15)
        layers.move_to(base_pos)
        
        # Output
        output_text = Text("Output: \"mat\"", font_size=16, color=RED)
        output_text.move_to(base_pos + UP * 1.5)
        
        # Animation
        self.play(FadeIn(input_text, shift=UP))
        self.wait(0.5)
        
        for layer in layers:
            self.play(FadeIn(layer, shift=UP))
            self.wait(0.3)
        
        self.wait(0.5)
        self.play(FadeIn(output_text, shift=UP))
        self.wait(1)
        
        # Clear the visual
        transformer_visual = VGroup(input_text, layers, output_text)
        self.play(FadeOut(transformer_visual))
    
    def training_process(self):
        """Fixed training process with proper equation positioning for 720p"""
        # Training title
        training_title = Text("Training Methodology", font_size=32, color=ORANGE, weight=BOLD)
        training_title.to_edge(UP, buff=1)
        
        # Pre-training section
        pretrain_title = Text("Pre-training: Language Modeling", font_size=26, color=BLUE)
        pretrain_title.move_to(UP * 1.5)
        
        pretrain_desc = Text("Predict next token given previous context", font_size=20, color=WHITE)
        pretrain_desc.next_to(pretrain_title, DOWN, buff=0.3)
        
        # Language modeling equation with proper spacing
        equation1 = MathTex(
            r"L_1(U) = \sum_i \log P(u_i | u_{i-k}, ..., u_{i-1}; \Theta)", 
            font_size=28, 
            color=WHITE
        )
        equation1.next_to(pretrain_desc, DOWN, buff=0.6)
        
        # Fine-tuning section
        finetune_title = Text("Fine-tuning: Task Adaptation", font_size=26, color=GREEN)
        finetune_title.next_to(equation1, DOWN, buff=1)
        
        finetune_desc = Text("Combine task loss with auxiliary language modeling", font_size=20, color=WHITE)
        finetune_desc.next_to(finetune_title, DOWN, buff=0.3)
        
        # Fine-tuning equation with proper spacing
        equation2 = MathTex(
            r"L_3(C) = L_2(C) + \lambda \cdot L_1(C)", 
            font_size=28, 
            color=WHITE
        )
        equation2.next_to(finetune_desc, DOWN, buff=0.6)
        
        # Animation
        self.play(FadeIn(training_title, shift=DOWN))
        self.wait(1)
        
        self.play(FadeIn(pretrain_title, shift=LEFT))
        self.play(Write(pretrain_desc))
        self.wait(0.5)
        self.play(Write(equation1))
        self.wait(1.5)
        
        self.play(FadeIn(finetune_title, shift=RIGHT))
        self.play(Write(finetune_desc))
        self.wait(0.5)
        self.play(Write(equation2))
        self.wait(2)
        
        # Clear for next section
        training_objects = VGroup(
            training_title, pretrain_title, pretrain_desc, equation1,
            finetune_title, finetune_desc, equation2
        )
        self.play(FadeOut(training_objects))
        self.wait(0.5)
    
    def key_results(self):
        """Improved results section for 720p"""
        # Results title
        results_title = Text("Breakthrough Performance", font_size=32, color=GREEN, weight=BOLD)
        results_title.to_edge(UP, buff=1)
        
        # Achievement highlight
        achievement = Text("State-of-the-art on 9 out of 12 tasks", 
                          font_size=28, color=YELLOW, weight=BOLD)
        achievement.next_to(results_title, DOWN, buff=1)
        
        # Key improvements table
        improvements = [
            ("Stories Cloze Test (Reasoning)", "+8.9%", BLUE),
            ("RACE (Reading Comprehension)", "+5.7%", GREEN),
            ("MultiNLI (Textual Entailment)", "+1.5%", RED),
            ("GLUE Benchmark (Overall)", "+5.5%", PURPLE)
        ]
        
        improvement_group = VGroup()
        for task, improvement, color in improvements:
            task_text = Text(task, font_size=22, color=WHITE)
            improvement_text = Text(improvement, font_size=26, color=color, weight=BOLD)
            
            improvement_row = VGroup(task_text, improvement_text)
            improvement_row.arrange(RIGHT, buff=1.5)
            improvement_group.add(improvement_row)
        
        improvement_group.arrange(DOWN, buff=0.6)
        improvement_group.next_to(achievement, DOWN, buff=1.2)
        
        # Animation
        self.play(FadeIn(results_title, shift=DOWN))
        self.wait(1)
        
        self.play(Write(achievement))
        self.wait(1.5)
        
        for improvement_row in improvement_group:
            self.play(FadeIn(improvement_row, shift=LEFT))
            self.wait(0.8)
        
        self.wait(2.5)
        
        # Clear for next section
        results_objects = VGroup(results_title, achievement, improvement_group)
        self.play(FadeOut(results_objects))
        self.wait(0.5)
    
    def impact_legacy(self):
        """FIXED timeline with correct parameter counts and proper spacing for 720p"""
        # Impact title
        impact_title = Text("The GPT Revolution", font_size=32, color=PURPLE, weight=BOLD)
        impact_title.to_edge(UP, buff=1)
        
        # Corrected timeline events with proper parameter values
        timeline_events = [
            ("GPT-1", "2018", "117M", BLUE),
            ("GPT-2", "2019", "1.5B", GREEN),
            ("GPT-3", "2020", "175B", YELLOW),
            ("ChatGPT", "2022", "Changed everything", RED)
        ]
        
        timeline = VGroup()
        for i, (model, year, description, color) in enumerate(timeline_events):
            # Event circle
            circle = Circle(radius=0.2, color=color, fill_opacity=0.8)
            
            # Model name
            model_text = Text(model, font_size=20, color=WHITE, weight=BOLD)
            model_text.next_to(circle, UP, buff=0.3)
            
            # Year
            year_text = Text(year, font_size=18, color=color, weight=BOLD)
            year_text.next_to(circle, DOWN, buff=0.15)
            
            # Description - FIXED to show correct parameter counts
            if i < 3:  # For GPT models, add "parameters" suffix
                desc_text = Text(f"{description} parameters", font_size=14, color=GRAY)
            else:  # For ChatGPT, keep original description
                desc_text = Text(description, font_size=14, color=GRAY)
            desc_text.next_to(year_text, DOWN, buff=0.15)
            
            event_group = VGroup(circle, model_text, year_text, desc_text)
            timeline.add(event_group)
        
        # Arrange timeline with proper spacing for 720p
        timeline.arrange(RIGHT, buff=1.5)
        timeline.move_to(ORIGIN + DOWN * 0.3)
        
        # Connecting line
        line_start = timeline[0][0].get_center()
        line_end = timeline[-1][0].get_center()
        line = Line(start=line_start, end=line_end, color=WHITE, stroke_width=3)
        
        # Animation
        self.play(FadeIn(impact_title, shift=DOWN))
        self.wait(1)
        
        self.play(Create(line))
        self.wait(0.5)
        
        for i, event_group in enumerate(timeline):
            self.play(FadeIn(event_group, shift=UP))
            self.wait(0.8)
        
        self.wait(2.5)
        
        # Clear for conclusion
        impact_objects = VGroup(impact_title, timeline, line)
        self.play(FadeOut(impact_objects))
        self.wait(0.5)
    
    def conclusion(self):
        """FIXED conclusion with proper text boundaries for 720p"""
        # Conclusion title
        conclusion_title = Text("Key Takeaways", font_size=32, color=GREEN, weight=BOLD)
        conclusion_title.to_edge(UP, buff=1)
        
        # Key points with proper bullet formatting and contained within frame
        takeaways = [
            "Demonstrated power of unsupervised pre-training",
            "Showed transformers excel at language modeling", 
            "Proved transfer learning works for NLP",
            "Laid foundation for modern LLMs"
        ]
        
        takeaway_group = VGroup()
        for takeaway in takeaways:
            bullet = Text("•", font_size=28, color=YELLOW, weight=BOLD)
            # Reduced font size to ensure text fits within 720p frame
            takeaway_text = Text(takeaway, font_size=22, color=WHITE)
            
            takeaway_row = VGroup(bullet, takeaway_text)
            takeaway_row.arrange(RIGHT, buff=0.3)
            takeaway_group.add(takeaway_row)
        
        takeaway_group.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        takeaway_group.next_to(conclusion_title, DOWN, buff=1.2)
        # Center the takeaways properly within the frame
        takeaway_group.move_to(ORIGIN + DOWN * 0.5)
        
        # Final message
        final_message = Text(
            "The Beginning of the AI Revolution", 
            font_size=28, 
            color=YELLOW, 
            weight=BOLD
        )
        final_message.to_edge(DOWN, buff=1.2)
        
        # Animation
        self.play(FadeIn(conclusion_title, shift=DOWN))
        self.wait(1)
        
        for takeaway_row in takeaway_group:
            self.play(FadeIn(takeaway_row, shift=LEFT))
            self.wait(0.7)
        
        self.wait(1)
        self.play(FadeIn(final_message, scale=0.8))
        self.wait(3)
        
        # Final fade out
        conclusion_objects = VGroup(conclusion_title, takeaway_group, final_message)
        self.play(FadeOut(conclusion_objects))
        self.wait(1)

if __name__ == "__main__":
    # Configuration for 720p rendering
    config.quality = "high_quality"
    config.preview = True
    config.disable_caching = False
    config.output_file = "gpt_paper_animation_720p"
    
    # Render the scene
    scene = GPTPaperAnimation()
    scene.render()
