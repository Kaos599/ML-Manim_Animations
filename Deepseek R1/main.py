from manim import *
import numpy as np

# Configuration for high-quality output
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 30

# DeepSeek brand color palette (verified)
DEEPSEEK_BLUE = "#1E40AF"
DEEPSEEK_TEAL = "#0891B2" 
DEEPSEEK_LIGHT = "#3B82F6"
DEEPSEEK_DARK = "#1E293B"
ACCENT_GREEN = "#10B981"
ACCENT_ORANGE = "#F59E0B"
ACCENT_RED = "#EF4444"
ACCENT_PURPLE = "#8B5CF6"

class DeepSeekR1Animation(Scene):
    def construct(self):
        """
        One-minute animation showcasing DeepSeek-R1's revolutionary approach.
        Five scenes, 12 seconds each, focusing on key technical innovations.
        """
        self.camera.background_color = "#F8FAFC"
        
        # Execute five focused scenes
        self.paradigm_shift()         # 0-12s: Traditional vs Pure RL
        self.grpo_algorithm()         # 12-24s: GRPO mechanism  
        self.aha_moment()            # 24-36s: Emergent metacognition
        self.training_pipeline()     # 36-48s: Four-stage process
        self.performance_results()   # 48-60s: Results and impact
    
    def paradigm_shift(self):
        """Scene 1: Traditional supervised learning vs pure RL paradigm"""
        self.clear()
        
        # Scene title
        title = Text("DeepSeek-R1: Pure RL Reasoning Revolution", 
                    font_size=36, color=DEEPSEEK_BLUE, weight=BOLD)
        title.to_edge(UP, buff=0.8)
        
        self.play(FadeIn(title))
        self.wait(0.8)
        
        # Traditional approach (left side)
        trad_title = Text("Traditional Approach", font_size=28, color=ACCENT_RED, weight=BOLD)
        trad_title.move_to(LEFT * 4.5 + UP * 1.8)
        
        trad_pipeline = VGroup(
            self.create_pipeline_box("Massive Datasets", ACCENT_RED),
            Text("↓", font_size=24, color=ACCENT_RED),
            self.create_pipeline_box("Supervised Fine-tuning", ACCENT_RED),
            Text("↓", font_size=24, color=ACCENT_RED),
            self.create_pipeline_box("Limited RL", ACCENT_RED)
        )
        trad_pipeline.arrange(DOWN, buff=0.3)
        trad_pipeline.next_to(trad_title, DOWN, buff=0.8)
        
        # DeepSeek-R1 approach (right side)
        deepseek_title = Text("DeepSeek-R1 Approach", font_size=28, color=DEEPSEEK_BLUE, weight=BOLD)
        deepseek_title.move_to(RIGHT * 4.5 + UP * 1.8)
        
        deepseek_pipeline = VGroup(
            self.create_pipeline_box("Base Model", DEEPSEEK_BLUE),
            Text("↓", font_size=24, color=DEEPSEEK_BLUE),
            self.create_pipeline_box("Pure RL Training", DEEPSEEK_BLUE),
            Text("↓", font_size=24, color=DEEPSEEK_BLUE),
            self.create_pipeline_box("Reasoning Emergence", DEEPSEEK_BLUE)
        )
        deepseek_pipeline.arrange(DOWN, buff=0.3)
        deepseek_pipeline.next_to(deepseek_title, DOWN, buff=0.8)
        
        # Animate both approaches
        self.play(FadeIn(trad_title), FadeIn(deepseek_title))
        self.play(
            LaggedStartMap(FadeIn, trad_pipeline, lag_ratio=0.3),
            LaggedStartMap(FadeIn, deepseek_pipeline, lag_ratio=0.3)
        )
        self.wait(1)
        
        # Performance breakthrough highlight
        breakthrough = Text("AIME 2024: 15.6% → 71.0% through pure RL", 
                           font_size=24, color=ACCENT_GREEN, weight=BOLD)
        breakthrough.move_to(DOWN * 2.2)
        
        highlight = Text("First model to achieve o1-level reasoning without supervised fine-tuning", 
                        font_size=18, color=DEEPSEEK_TEAL)
        highlight.next_to(breakthrough, DOWN, buff=0.4)
        
        self.play(Write(breakthrough))
        self.play(FadeIn(highlight))
        self.wait(2)
        
        # Clear scene
        all_elements = VGroup(title, trad_title, trad_pipeline, deepseek_title, 
                             deepseek_pipeline, breakthrough, highlight)
        self.play(FadeOut(all_elements))
        self.wait(0.3)
    
    def grpo_algorithm(self):
        """Scene 2: Group Relative Policy Optimization mechanism"""
        self.clear()
        
        # Algorithm title
        algo_title = Text("GRPO: Group Relative Policy Optimization", 
                         font_size=32, color=DEEPSEEK_BLUE, weight=BOLD)
        algo_title.to_edge(UP, buff=0.8)
        
        self.play(FadeIn(algo_title))
        self.wait(0.8)
        
        # Core equation with annotation
        equation = MathTex(
            r"A_i = \frac{r_i - \bar{r}}{\sigma_r}",
            font_size=40,
            color=DEEPSEEK_BLUE
        )
        equation_box = SurroundingRectangle(equation, color=DEEPSEEK_TEAL, 
                                          fill_opacity=0.1, buff=0.5)
        equation_group = VGroup(equation_box, equation)
        equation_group.move_to(UP * 0.8)
        
        # Mathematical components breakdown
        components = VGroup(
            Text("A_i = Advantage for response i", font_size=16, color=DEEPSEEK_DARK),
            Text("r_i = Individual reward", font_size=16, color=DEEPSEEK_DARK),
            Text("r̄ = Group mean reward", font_size=16, color=DEEPSEEK_DARK),
            Text("σ_r = Group standard deviation", font_size=16, color=DEEPSEEK_DARK)
        )
        components.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        components.next_to(equation_group, DOWN, buff=0.8)
        
        # Group sampling visualization
        sampling_title = Text("Group Sampling Process", font_size=20, color=DEEPSEEK_TEAL, weight=BOLD)
        sampling_title.move_to(DOWN * 1.8)
        
        response_groups = VGroup()
        for i in range(4):
            response_box = Rectangle(width=1.8, height=0.6, color=DEEPSEEK_LIGHT, 
                                   fill_opacity=0.3, stroke_width=2)
            response_text = Text(f"Response {i+1}", font_size=14, color=DEEPSEEK_DARK, weight=BOLD)
            response_item = VGroup(response_box, response_text)
            response_groups.add(response_item)
        
        response_groups.arrange(RIGHT, buff=0.3)
        response_groups.next_to(sampling_title, DOWN, buff=0.5)
        
        # Key innovation highlight
        innovation = Text("No critic model needed - uses group statistics for efficiency", 
                         font_size=18, color=ACCENT_GREEN, weight=BOLD)
        innovation.to_edge(DOWN, buff=0.8)
        
        # Animate GRPO components
        self.play(FadeIn(equation_group))
        self.play(LaggedStartMap(FadeIn, components, lag_ratio=0.2))
        self.wait(1)
        
        self.play(FadeIn(sampling_title))
        self.play(LaggedStartMap(FadeIn, response_groups, lag_ratio=0.2))
        self.wait(1)
        
        self.play(Write(innovation))
        self.wait(2)
        
        # Clear scene
        grpo_elements = VGroup(algo_title, equation_group, components, 
                              sampling_title, response_groups, innovation)
        self.play(FadeOut(grpo_elements))
        self.wait(0.3)
    
    def aha_moment(self):
        """Scene 3: Emergent meta-cognitive reasoning phenomenon"""
        self.clear()
        
        # Scene title
        aha_title = Text("The \"Aha Moment\" Phenomenon", 
                        font_size=32, color=DEEPSEEK_BLUE, weight=BOLD)
        aha_title.to_edge(UP, buff=0.8)
        
        self.play(FadeIn(aha_title))
        self.wait(0.8)
        
        # Actual quote from paper with emphasis
        quote_box = Rectangle(width=13, height=1.8, color=ACCENT_ORANGE, 
                             fill_opacity=0.1, stroke_width=3)
        quote_text = Text("\"Wait, wait. That's an aha moment I can flag here.\nLet's reevaluate this step-by-step...\"", 
                         font_size=18, color=ACCENT_ORANGE, weight=BOLD, 
                         line_spacing=1.2)
        quote_group = VGroup(quote_box, quote_text)
        quote_group.move_to(UP * 1.2)
        
        # Metacognitive development process
        metacognition_title = Text("Emergent Metacognitive Development", 
                                  font_size=20, color=DEEPSEEK_TEAL, weight=BOLD)
        metacognition_title.move_to(DOWN * 0.2)
        
        thinking_evolution = VGroup(
            Text("1. Initial problem-solving attempt", font_size=16, color=DEEPSEEK_DARK),
            Text("2. Self-recognition of potential errors", font_size=16, color=DEEPSEEK_DARK),
            Text("3. Strategic approach reevaluation", font_size=16, color=DEEPSEEK_DARK),
            Text("4. Alternative solution exploration", font_size=16, color=DEEPSEEK_DARK)
        )
        thinking_evolution.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        thinking_evolution.next_to(metacognition_title, DOWN, buff=0.6)
        
        # Key insight
        insight = Text("Emerges naturally through RL - no explicit programming required", 
                      font_size=18, color=ACCENT_GREEN, weight=BOLD)
        insight.to_edge(DOWN, buff=0.8)
        
        # Animate emergence
        self.play(FadeIn(quote_group))
        self.wait(1.5)
        
        self.play(FadeIn(metacognition_title))
        self.play(LaggedStartMap(FadeIn, thinking_evolution, lag_ratio=0.4))
        self.wait(1)
        
        self.play(Write(insight))
        self.wait(2)
        
        # Clear scene
        aha_elements = VGroup(aha_title, quote_group, metacognition_title, 
                             thinking_evolution, insight)
        self.play(FadeOut(aha_elements))
        self.wait(0.3)
    
    def training_pipeline(self):
        """Scene 4: Four-stage training process"""
        self.clear()
        
        # Pipeline title
        pipeline_title = Text("Four-Stage Training Pipeline", 
                             font_size=32, color=DEEPSEEK_BLUE, weight=BOLD)
        pipeline_title.to_edge(UP, buff=0.8)
        
        self.play(FadeIn(pipeline_title))
        self.wait(0.8)
        
        # Training stages with proper spacing
        stages = [
            ("Stage 1", "Cold Start", "SFT on curated CoT data", DEEPSEEK_BLUE),
            ("Stage 2", "Reasoning RL", "GRPO with rule-based rewards", DEEPSEEK_TEAL),
            ("Stage 3", "Rejection Sampling", "Data filtering + comprehensive SFT", ACCENT_GREEN),
            ("Stage 4", "Multi-scenario RL", "Final alignment training", ACCENT_PURPLE)
        ]
        
        stage_elements = VGroup()
        stage_arrows = VGroup()
        
        for i, (stage_num, stage_name, description, color) in enumerate(stages):
            # Stage container
            stage_box = Rectangle(width=4, height=1.4, color=color, fill_opacity=0.2, stroke_width=2)
            stage_box.move_to(LEFT * 6 + RIGHT * i * 3.2)
            
            # Stage labels
            num_text = Text(stage_num, font_size=14, color=color, weight=BOLD)
            name_text = Text(stage_name, font_size=16, color=color, weight=BOLD)
            desc_text = Text(description, font_size=12, color=DEEPSEEK_DARK, line_spacing=1.1)
            
            stage_content = VGroup(num_text, name_text, desc_text)
            stage_content.arrange(DOWN, buff=0.1)
            stage_content.move_to(stage_box.get_center())
            
            stage_item = VGroup(stage_box, stage_content)
            stage_elements.add(stage_item)
            
            # Arrow between stages
            if i < len(stages) - 1:
                arrow = Arrow(
                    start=stage_box.get_right() + RIGHT * 0.1,
                    end=LEFT * 6 + RIGHT * (i + 1) * 3.2 + LEFT * 2 + LEFT * 0.1,
                    color=DEEPSEEK_DARK,
                    stroke_width=3
                )
                stage_arrows.add(arrow)
        
        # Key achievement
        achievement = Text("Language consistency through reward engineering", 
                          font_size=18, color=ACCENT_ORANGE, weight=BOLD)
        achievement.to_edge(DOWN, buff=0.8)
        
        # Animate pipeline construction
        self.play(LaggedStartMap(FadeIn, stage_elements, lag_ratio=0.3))
        self.play(LaggedStartMap(GrowArrow, stage_arrows, lag_ratio=0.2))
        self.wait(1)
        
        self.play(FadeIn(achievement))
        self.wait(2)
        
        # Clear scene
        pipeline_elements = VGroup(pipeline_title, stage_elements, stage_arrows, achievement)
        self.play(FadeOut(pipeline_elements))
        self.wait(0.3)
    
    def performance_results(self):
        """Scene 5: Breakthrough results and distillation impact"""
        self.clear()
        
        # Results title
        results_title = Text("Breakthrough Performance & Open Source Impact", 
                            font_size=30, color=DEEPSEEK_BLUE, weight=BOLD)
        results_title.to_edge(UP, buff=0.8)
        
        self.play(FadeIn(results_title))
        self.wait(0.8)
        
        # Performance comparison with verified data
        benchmarks = [
            ("AIME 2024", [79.8, 79.2], ["DeepSeek-R1", "OpenAI o1-1217"]),
            ("MATH-500", [97.3, 96.4], ["DeepSeek-R1", "OpenAI o1-1217"]),
            ("Codeforces", [96.3, 96.6], ["DeepSeek-R1", "OpenAI o1-1217"])
        ]
        
        # Create performance chart
        chart_y = UP * 1.2
        for i, (benchmark, scores, models) in enumerate(benchmarks):
            bench_title = Text(benchmark, font_size=16, color=DEEPSEEK_BLUE, weight=BOLD)
            bench_title.move_to(LEFT * 5 + chart_y + DOWN * i * 1.2)
            
            # Performance bars
            for j, (score, model) in enumerate(zip(scores, models)):
                bar_width = (score / 100) * 3
                bar_color = DEEPSEEK_TEAL if j == 0 else ACCENT_ORANGE
                
                bar = Rectangle(width=bar_width, height=0.3, color=bar_color, fill_opacity=0.7)
                bar.move_to(LEFT * 2 + RIGHT * bar_width/2 + chart_y + DOWN * i * 1.2 + DOWN * j * 0.4)
                
                score_label = Text(f"{score:.1f}%", font_size=12, color=WHITE, weight=BOLD)
                score_label.move_to(bar.get_center())
                
                self.add(bench_title, bar, score_label)
        
        # Distillation success
        distillation_title = Text("Distillation Success", font_size=20, color=DEEPSEEK_TEAL, weight=BOLD)
        distillation_title.move_to(RIGHT * 3 + UP * 1)
        
        distillation_points = VGroup(
            Text("• 98% cost reduction", font_size=16, color=ACCENT_GREEN),
            Text("• 1.5B to 70B model variants", font_size=16, color=ACCENT_GREEN),
            Text("• Open source availability", font_size=16, color=ACCENT_GREEN),
            Text("• Reasoning pattern transfer", font_size=16, color=ACCENT_GREEN)
        )
        distillation_points.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        distillation_points.next_to(distillation_title, DOWN, buff=0.5)
        
        # Impact statement
        impact = Text("Democratizing advanced reasoning capabilities worldwide", 
                     font_size=18, color=DEEPSEEK_BLUE, weight=BOLD)
        impact.to_edge(DOWN, buff=0.8)
        
        # Animate results
        self.wait(1)  # Allow chart to be visible
        self.play(FadeIn(distillation_title))
        self.play(LaggedStartMap(FadeIn, distillation_points, lag_ratio=0.3))
        self.wait(1)
        
        self.play(Write(impact))
        self.wait(2.5)
        
        # Final fade
        self.play(FadeOut(VGroup(results_title, distillation_title, distillation_points, impact)))
        self.wait(0.5)
    
    def create_pipeline_box(self, text, color):
        """Helper function to create consistent pipeline boxes"""
        box = Rectangle(width=3, height=0.8, color=color, fill_opacity=0.2, stroke_width=2)
        label = Text(text, font_size=14, color=color, weight=BOLD)
        return VGroup(box, label)

if __name__ == "__main__":
    """
    Production configuration for DeepSeek-R1 animation.
    Academic presentation focusing on key technical breakthroughs.
    """
    config.quality = "high_quality"
    config.preview = True
    config.disable_caching = False
    config.output_file = "deepseek_r1"
    
    scene = DeepSeekR1Animation()
    scene.render()
