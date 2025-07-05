from manim import *
import numpy as np

# Configuration for high-quality output
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 30

# Meta AI brand color palette
META_BLUE = "#1877F2"
META_TEAL = "#42A5F5"
META_DARK_BLUE = "#166FE5"
META_LIGHT_BLUE = "#E3F2FD"
ACCENT_ORANGE = "#FF6B35"
ACCENT_GREEN = "#4CAF50"
ACCENT_RED = "#F44336"
ACCENT_PURPLE = "#9C27B0"

class LlamaThreeAnimation(Scene):
    def construct(self):
        """
        Main animation sequence for Meta Llama 3 research presentation.
        Covers training methodology, performance results, and key innovations.
        """
        self.camera.background_color = "#F8F9FA"
        
        # Execute animation sequence
        self.opening_hook()
        self.training_pipeline_visualization()
        self.dpo_vs_ppo_comparison()
        self.multilingual_training_strategy()
        self.context_window_expansion()
        self.results_and_impact()
        self.conclusion()
    
    def opening_hook(self):
        """Introduction scene showing evolution from traditional to unified LLMs"""
        self.clear()
        
        # Title sequence
        title = Text("The Llama 3 Herd of Models", font_size=48, color=META_BLUE, weight=BOLD)
        subtitle = Text("Meta's Revolutionary Multimodal AI Architecture", font_size=28, color=META_TEAL)
        
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        title_group.move_to(ORIGIN)
        
        self.play(FadeIn(title_group, shift=UP))
        self.wait(2)
        self.play(FadeOut(title_group))
        
        # Traditional LLM limitations
        problem_title = Text("Traditional LLM Limitations", font_size=36, color=ACCENT_RED, weight=BOLD)
        problem_title.to_edge(UP, buff=1)
        
        # Create modality silos with proper spacing
        text_silo = self.create_silo("Text\nProcessing", META_BLUE, LEFT * 4.5)
        image_silo = self.create_silo("Image\nAnalysis", ACCENT_GREEN, ORIGIN)
        speech_silo = self.create_silo("Speech\nRecognition", ACCENT_PURPLE, RIGHT * 4.5)
        
        # Isolation barriers
        barrier1 = Line(LEFT * 2.5 + UP * 2, LEFT * 2.5 + DOWN * 2, color=ACCENT_RED, stroke_width=8)
        barrier2 = Line(RIGHT * 2.5 + UP * 2, RIGHT * 2.5 + DOWN * 2, color=ACCENT_RED, stroke_width=8)
        
        self.play(FadeIn(problem_title))
        self.wait(1)
        
        self.play(LaggedStartMap(FadeIn, [text_silo, image_silo, speech_silo], lag_ratio=0.3))
        self.wait(1)
        
        self.play(Create(barrier1), Create(barrier2))
        self.wait(1)
        
        # Transition to unified approach
        solution_title = Text("Llama 3's Unified Approach", font_size=36, color=META_BLUE, weight=BOLD)
        solution_title.to_edge(UP, buff=1)
        
        self.play(
            Transform(problem_title, solution_title),
            FadeOut(barrier1),
            FadeOut(barrier2)
        )
        
        # Unified architecture
        unified_core = Circle(radius=1.8, color=META_BLUE, fill_opacity=0.3)
        unified_label = Text("Llama 3\nUnified Core", font_size=24, color=WHITE, weight=BOLD)
        unified_group = VGroup(unified_core, unified_label)
        
        self.play(
            Transform(VGroup(text_silo, image_silo, speech_silo), unified_group),
            run_time=2
        )
        
        # Capability labels with proper spacing
        capabilities = [
            "Text Generation", "Image Understanding", "Speech Processing",
            "Multimodal Reasoning", "Cross-Modal Transfer", "Unified Learning"
        ]
        
        capability_labels = VGroup()
        for i, cap in enumerate(capabilities):
            angle = i * TAU / len(capabilities)
            pos = 3.2 * (np.cos(angle) * RIGHT + np.sin(angle) * UP)
            label = Text(cap, font_size=16, color=META_DARK_BLUE, weight=BOLD)
            label.move_to(pos)
            capability_labels.add(label)
        
        self.play(LaggedStartMap(FadeIn, capability_labels, lag_ratio=0.2))
        
        # Connection lines
        connection_lines = VGroup()
        for label in capability_labels:
            direction = label.get_center() - unified_core.get_center()
            direction_normalized = direction / np.linalg.norm(direction)
            start_point = unified_core.get_center() + direction_normalized * 1.8
            
            line = Line(start_point, label.get_center(), color=META_TEAL, stroke_width=2)
            connection_lines.add(line)
        
        self.play(LaggedStartMap(Create, connection_lines, lag_ratio=0.1))
        self.wait(2)
        
        # Scene cleanup
        all_elements = VGroup(
            unified_group, capability_labels, connection_lines, problem_title
        )
        self.play(FadeOut(all_elements))
        self.wait(0.5)
    
    def create_silo(self, label_text, color, position):
        """Create modality silo visualization"""
        silo = Rectangle(width=2, height=3, color=color, fill_opacity=0.2)
        label = Text(label_text, font_size=20, color=color, weight=BOLD)
        silo_group = VGroup(silo, label)
        silo_group.move_to(position)
        return silo_group
    
    def training_pipeline_visualization(self):
        """Visualization of the complete training pipeline"""
        self.clear()
        
        pipeline_title = Text("Llama 3 Training Pipeline", font_size=40, color=META_BLUE, weight=BOLD)
        pipeline_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(pipeline_title))
        self.wait(1)
        
        # Training stages with verified specifications
        stages = [
            ("Pre-training", "15.6T tokens", META_BLUE),
            ("Supervised\nFine-tuning", "Instruction\nFollowing", META_TEAL),
            ("Rejection\nSampling", "Quality\nFiltering", ACCENT_GREEN),
            ("PPO", "Policy\nOptimization", ACCENT_ORANGE),
            ("DPO", "Direct\nPreference", ACCENT_PURPLE)
        ]
        
        # Create pipeline components
        stage_boxes = VGroup()
        stage_labels = VGroup()
        stage_details = VGroup()
        
        x_positions = np.linspace(-6, 6, len(stages))
        
        for i, (stage, detail, color) in enumerate(stages):
            box = Rectangle(width=2.2, height=1.8, color=color, fill_opacity=0.3)
            box.move_to(x_positions[i] * RIGHT + UP * 1)
            
            label = Text(stage, font_size=18, color=color, weight=BOLD, line_spacing=1.2)
            label.move_to(box.get_center())
            
            detail_text = Text(detail, font_size=14, color=DARK_GRAY, line_spacing=1.2)
            detail_text.next_to(box, DOWN, buff=0.4)
            
            stage_boxes.add(box)
            stage_labels.add(label)
            stage_details.add(detail_text)
        
        # Animate pipeline construction
        self.play(LaggedStartMap(FadeIn, stage_boxes, lag_ratio=0.2))
        self.play(LaggedStartMap(Write, stage_labels, lag_ratio=0.2))
        self.play(LaggedStartMap(FadeIn, stage_details, lag_ratio=0.2))
        
        # Inter-stage connections
        arrows = VGroup()
        for i in range(len(stages) - 1):
            arrow = Arrow(
                start=stage_boxes[i].get_right() + RIGHT * 0.1,
                end=stage_boxes[i + 1].get_left() + LEFT * 0.1,
                color=META_DARK_BLUE,
                stroke_width=4
            )
            arrows.add(arrow)
        
        self.play(LaggedStartMap(GrowArrow, arrows, lag_ratio=0.2))
        
        # Training scale statistics
        stats_title = Text("Training Scale", font_size=24, color=META_BLUE, weight=BOLD)
        stats_title.to_edge(DOWN, buff=2.5)
        
        stats = [
            "15.6 Trillion Tokens", "405 Billion Parameters", 
            "128K Context Window", "16K H100 GPUs"
        ]
        
        stats_group = VGroup()
        for stat in stats:
            stat_box = Rectangle(width=2.8, height=0.8, color=META_TEAL, fill_opacity=0.1)
            stat_text = Text(stat, font_size=14, color=META_DARK_BLUE, weight=BOLD)
            stat_item = VGroup(stat_box, stat_text)
            stats_group.add(stat_item)
        
        stats_group.arrange(RIGHT, buff=0.3)
        stats_group.next_to(stats_title, DOWN, buff=0.5)
        
        self.play(FadeIn(stats_title))
        self.play(LaggedStartMap(FadeIn, stats_group, lag_ratio=0.2))
        self.wait(3)
        
        # Scene cleanup
        pipeline_elements = VGroup(
            pipeline_title, stage_boxes, stage_labels, stage_details, 
            arrows, stats_title, stats_group
        )
        self.play(FadeOut(pipeline_elements))
        self.wait(0.5)
    
    def dpo_vs_ppo_comparison(self):
        """Comparison of DPO and PPO training methodologies"""
        self.clear()
        
        # Repositioned title to prevent overlap
        comparison_title = Text("DPO vs PPO: Training Methodology", font_size=36, color=META_BLUE, weight=BOLD)
        comparison_title.to_edge(UP, buff=0.8)  # Moved higher to prevent overlap
        
        self.play(FadeIn(comparison_title))
        self.wait(1)
        
        # PPO section
        ppo_title = Text("PPO: Policy Gradient", font_size=28, color=ACCENT_ORANGE, weight=BOLD)
        ppo_title.move_to(LEFT * 4 + UP * 2)  # Adjusted position
        
        ppo_features = [
            "• Trial-and-error learning",
            "• Gradual policy updates", 
            "• Reward model required",
            "• Multiple sampling rounds",
            "• Stable but slower convergence"
        ]
        
        ppo_list = VGroup()
        for feature in ppo_features:
            feature_text = Text(feature, font_size=16, color=DARK_GRAY)
            ppo_list.add(feature_text)
        
        ppo_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        ppo_list.next_to(ppo_title, DOWN, buff=0.6)
        
        # PPO equation with surrounding box
        ppo_equation = MathTex(
            r"L^{CLIP}(\theta) = \hat{\mathbb{E}}_t[\min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)]",
            font_size=18,
            color=ACCENT_ORANGE
        )
        
        ppo_box = SurroundingRectangle(ppo_equation, color=ACCENT_ORANGE, fill_opacity=0.1, buff=0.3)
        ppo_eq_group = VGroup(ppo_box, ppo_equation)
        ppo_eq_group.next_to(ppo_list, DOWN, buff=0.6)
        
        # DPO section
        dpo_title = Text("DPO: Direct Optimization", font_size=28, color=ACCENT_PURPLE, weight=BOLD)
        dpo_title.move_to(RIGHT * 4 + UP * 2)  # Adjusted position
        
        dpo_features = [
            "• Direct preference ranking",
            "• Single-step optimization",
            "• No reward model needed",
            "• Preference pair training",
            "• Faster, more efficient"
        ]
        
        dpo_list = VGroup()
        for feature in dpo_features:
            feature_text = Text(feature, font_size=16, color=DARK_GRAY)
            dpo_list.add(feature_text)
        
        dpo_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        dpo_list.next_to(dpo_title, DOWN, buff=0.6)
        
        # DPO equation with surrounding box
        dpo_equation = MathTex(
            r"L_{DPO}(\pi_\theta) = -\mathbb{E}_{(x,y_w,y_l) \sim \mathcal{D}}[\log \sigma(\beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)})]",
            font_size=14,
            color=ACCENT_PURPLE
        )
        
        dpo_box = SurroundingRectangle(dpo_equation, color=ACCENT_PURPLE, fill_opacity=0.1, buff=0.3)
        dpo_eq_group = VGroup(dpo_box, dpo_equation)
        dpo_eq_group.next_to(dpo_list, DOWN, buff=0.6)
        
        # Animate sections
        self.play(FadeIn(ppo_title))
        for feature in ppo_list:
            self.play(FadeIn(feature), run_time=0.3)
        self.play(FadeIn(ppo_eq_group))
        self.wait(1)
        
        self.play(FadeIn(dpo_title))
        for feature in dpo_list:
            self.play(FadeIn(feature), run_time=0.3)
        self.play(FadeIn(dpo_eq_group))
        self.wait(1)
        
        # Sequential application explanation
        sequential_title = Text("Sequential Application: Best of Both", font_size=24, color=META_BLUE, weight=BOLD)
        sequential_title.move_to(DOWN * 2.8)
        
        sequential_benefits = Text(
            "PPO establishes stable foundation → DPO fine-tunes preferences efficiently",
            font_size=18,
            color=META_TEAL
        )
        sequential_benefits.next_to(sequential_title, DOWN, buff=0.4)
        
        flow_arrow = Arrow(
            start=LEFT * 2 + DOWN * 2.2,
            end=RIGHT * 2 + DOWN * 2.2,
            color=META_BLUE,
            stroke_width=6
        )
        
        self.play(FadeIn(sequential_title))
        self.play(Write(sequential_benefits))
        self.play(GrowArrow(flow_arrow))
        self.wait(2)
        
        # Scene cleanup
        comparison_elements = VGroup(
            comparison_title, ppo_title, ppo_list, ppo_eq_group,
            dpo_title, dpo_list, dpo_eq_group, sequential_title,
            sequential_benefits, flow_arrow
        )
        self.play(FadeOut(comparison_elements))
        self.wait(0.5)
    
    def multilingual_training_strategy(self):
        """Multilingual capabilities and training approach"""
        self.clear()
        
        multilingual_title = Text("Multilingual Training Strategy", font_size=36, color=META_BLUE, weight=BOLD)
        multilingual_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(multilingual_title))
        self.wait(1)
        
        # Data composition visualization
        english_sector = Sector(
            start_angle=0, angle=0.95 * TAU, 
            color=META_BLUE, fill_opacity=0.7, radius=2
        )
        english_label = Text("95% English", font_size=18, color=WHITE, weight=BOLD)
        english_label.move_to(english_sector.get_center() + LEFT * 0.5)
        
        multilingual_sector = Sector(
            start_angle=0.95 * TAU, angle=0.05 * TAU,
            color=ACCENT_GREEN, fill_opacity=0.7, radius=2
        )
        multilingual_label = Text("5% Multilingual", font_size=16, color=WHITE, weight=BOLD)
        multilingual_label.move_to(multilingual_sector.get_center() + UP * 0.3)
        
        data_chart = VGroup(english_sector, multilingual_sector, english_label, multilingual_label)
        data_chart.move_to(LEFT * 4 + DOWN * 0.5)
        
        self.play(Create(english_sector), Write(english_label))
        self.play(Create(multilingual_sector), Write(multilingual_label))
        self.wait(1)
        
        # Language coverage
        languages_title = Text("30+ Languages Supported", font_size=24, color=META_TEAL, weight=BOLD)
        languages_title.move_to(RIGHT * 3 + UP * 1.5)
        
        sample_languages = [
            "English", "Spanish", "French", "German", "Italian",
            "Portuguese", "Hindi", "Thai", "Chinese", "Japanese",
            "Arabic", "Russian", "Korean", "Dutch", "Swedish"
        ]
        
        language_grid = VGroup()
        for i, lang in enumerate(sample_languages[:12]):
            lang_box = Rectangle(width=1.8, height=0.4, color=ACCENT_GREEN, fill_opacity=0.2)
            lang_text = Text(lang, font_size=12, color=ACCENT_GREEN, weight=BOLD)
            lang_item = VGroup(lang_box, lang_text)
            language_grid.add(lang_item)
        
        language_grid.arrange_in_grid(rows=4, cols=3, buff=0.1)
        language_grid.next_to(languages_title, DOWN, buff=0.5)
        
        self.play(FadeIn(languages_title))
        self.play(LaggedStartMap(FadeIn, language_grid, lag_ratio=0.1))
        self.wait(2)
        
        # Scene cleanup
        multilingual_elements = VGroup(
            multilingual_title, data_chart, languages_title, language_grid
        )
        self.play(FadeOut(multilingual_elements))
        self.wait(0.5)
    
    def context_window_expansion(self):
        """Context window scaling from 8K to 128K tokens"""
        self.clear()
        
        context_title = Text("Context Window Expansion", font_size=36, color=META_BLUE, weight=BOLD)
        context_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(context_title))
        self.wait(1)
        
        # Expansion stages
        stages = [
            ("8K", "Base Training", 1),
            ("16K", "Stage 1", 2),
            ("32K", "Stage 2", 3),
            ("64K", "Stage 3", 4),
            ("128K", "Final Stage", 5)
        ]
        
        # Create progression bars
        base_width = 0.5
        stage_bars = VGroup()
        stage_labels = VGroup()
        
        for i, (size, stage, multiplier) in enumerate(stages):
            bar_width = base_width * multiplier
            
            bar = Rectangle(
                width=bar_width, 
                height=0.6, 
                color=META_BLUE, 
                fill_opacity=0.7
            )
            bar.move_to(DOWN * (i - 2) * 1.2 + LEFT * 3)
            
            size_label = Text(size, font_size=20, color=WHITE, weight=BOLD)
            size_label.move_to(bar.get_center())
            
            stage_label = Text(stage, font_size=16, color=META_TEAL)
            stage_label.next_to(bar, RIGHT, buff=0.5)
            
            stage_bars.add(bar)
            stage_labels.add(VGroup(size_label, stage_label))
        
        # Animate expansion
        for i, (bar, label) in enumerate(zip(stage_bars, stage_labels)):
            self.play(GrowFromEdge(bar, LEFT), run_time=0.8)
            self.play(FadeIn(label), run_time=0.3)
            self.wait(0.2)
        
        # Training strategy
        strategy_title = Text("Staged Training Strategy", font_size=24, color=META_TEAL, weight=BOLD)
        strategy_title.move_to(RIGHT * 3.5 + UP * 1.5)
        
        strategy_points = [
            "1. Local patterns first",
            "2. Gradual expansion", 
            "3. Long-range dependencies",
            "4. Progressive complexity"
        ]
        
        strategy_list = VGroup()
        for point in strategy_points:
            point_text = Text(point, font_size=16, color=DARK_GRAY)
            strategy_list.add(point_text)
        
        strategy_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        strategy_list.next_to(strategy_title, DOWN, buff=0.5)
        
        # Applications
        applications_title = Text("Applications", font_size=24, color=META_BLUE, weight=BOLD)
        applications_title.move_to(RIGHT * 3.5 + DOWN * 1.5)
        
        applications = [
            "📄 Document Analysis",
            "💻 Code Processing", 
            "🗣️ Multi-turn Conversations",
            "📚 Research Papers"
        ]
        
        app_list = VGroup()
        for app in applications:
            app_text = Text(app, font_size=16, color=DARK_GRAY)
            app_list.add(app_text)
        
        app_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        app_list.next_to(applications_title, DOWN, buff=0.5)
        
        self.play(FadeIn(strategy_title))
        self.play(LaggedStartMap(FadeIn, strategy_list, lag_ratio=0.3))
        self.wait(1)
        
        self.play(FadeIn(applications_title))
        self.play(LaggedStartMap(FadeIn, app_list, lag_ratio=0.3))
        self.wait(2)
        
        # Scene cleanup
        context_elements = VGroup(
            context_title, stage_bars, stage_labels, strategy_title,
            strategy_list, applications_title, app_list
        )
        self.play(FadeOut(context_elements))
        self.wait(0.5)
    
    def results_and_impact(self):
        """Performance benchmarks and comparison results"""
        self.clear()
        
        results_title = Text("Llama 3 Performance Results", font_size=36, color=META_BLUE, weight=BOLD)
        results_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(results_title))
        self.wait(1)
        
        # Benchmark data with proper spacing
        benchmarks = [
            ("MMLU", [85.2, 83.1, 79.3], ["Llama 3 405B", "GPT-4", "Llama 3 70B"]),
            ("HumanEval", [89.0, 87.2, 80.5], ["Llama 3 405B", "GPT-4", "Llama 3 70B"]),
            ("MATH", [73.8, 72.6, 64.2], ["Llama 3 405B", "GPT-4", "Llama 3 70B"])
        ]
        
        # Create charts with proper bar spacing
        chart_y_start = UP * 1
        chart_spacing = 2.2  # Increased spacing to prevent overlap
        
        all_chart_elements = VGroup()
        
        for i, (benchmark, scores, models) in enumerate(benchmarks):
            chart_y = chart_y_start + DOWN * i * chart_spacing
            
            bench_title = Text(benchmark, font_size=20, color=META_BLUE, weight=BOLD)
            bench_title.move_to(LEFT * 6 + chart_y)
            
            # Create bars with increased vertical spacing
            bars = VGroup()
            labels = VGroup()
            
            colors = [META_BLUE, ACCENT_ORANGE, META_TEAL]
            max_score = max(scores)
            
            for j, (score, model, color) in enumerate(zip(scores, models, colors)):
                bar_width = (score / max_score) * 4
                bar = Rectangle(
                    width=bar_width, 
                    height=0.35,  # Reduced height to prevent overlap
                    color=color, 
                    fill_opacity=0.7
                )
                # Increased vertical spacing between bars
                bar.move_to(LEFT * 3 + RIGHT * bar_width/2 + chart_y + DOWN * j * 0.8)
                
                score_label = Text(f"{score:.1f}", font_size=14, color=color, weight=BOLD)
                score_label.next_to(bar, RIGHT, buff=0.2)
                
                model_label = Text(model, font_size=12, color=DARK_GRAY)
                model_label.next_to(bar, LEFT, buff=0.2)
                
                bars.add(bar)
                labels.add(VGroup(score_label, model_label))
            
            chart_group = VGroup(bench_title, bars, labels)
            all_chart_elements.add(chart_group)
            
            self.play(FadeIn(bench_title))
            self.play(LaggedStartMap(Create, bars, lag_ratio=0.2))
            self.play(LaggedStartMap(FadeIn, labels, lag_ratio=0.2))
            self.wait(0.5)
        
        # Impact statement positioned below all charts
        impact_statement = Text(
            "First open-source model to match GPT-4 across major benchmarks",
            font_size=20,
            color=META_BLUE,
            weight=BOLD
        )
        impact_statement.move_to(DOWN * 3.8)  # Moved further down to avoid overlap
        
        self.play(Write(impact_statement))
        self.wait(3)
        
        # Scene cleanup
        results_elements = VGroup(results_title, all_chart_elements, impact_statement)
        self.play(FadeOut(results_elements))
        self.wait(0.5)
    
    def conclusion(self):
        """Summary of key innovations and impact"""
        self.clear()
        
        conclusion_title = Text("The Llama 3 Revolution", font_size=40, color=META_BLUE, weight=BOLD)
        conclusion_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(conclusion_title))
        self.wait(1)
        
        # Key innovations with adjusted positioning
        innovations_title = Text("Key Innovations", font_size=28, color=META_TEAL, weight=BOLD)
        innovations_title.move_to(UP * 2.2)  # Moved up to create space
        
        innovations = [
            "Unified multimodal architecture",
            "Advanced training pipeline (SFT→RS→PPO→DPO)", 
            "Massive scale: 405B parameters, 15.6T tokens",
            "Extended context: 8K → 128K tokens",
            "Multilingual foundation with cross-lingual transfer",
            "GPT-4 level performance in open-source"
        ]
        
        innovation_items = VGroup()
        for innovation in innovations:
            bullet = Text("•", font_size=24, color=META_BLUE, weight=BOLD)
            text = Text(innovation, font_size=18, color=DARK_GRAY)
            
            item = VGroup(bullet, text)
            item.arrange(RIGHT, buff=0.3)
            innovation_items.add(item)
        
        innovation_items.arrange(DOWN, buff=0.35, aligned_edge=LEFT)  # Reduced spacing
        innovation_items.next_to(innovations_title, DOWN, buff=0.8)
        
        self.play(FadeIn(innovations_title))
        self.play(LaggedStartMap(FadeIn, innovation_items, lag_ratio=0.3))
        self.wait(2)
        
        # Impact section repositioned below
        future_title = Text("Impact on AI Development", font_size=24, color=ACCENT_GREEN, weight=BOLD)
        future_title.move_to(DOWN * 2.2)  # Moved down to avoid overlap
        
        future_text = Text(
            "Democratizing state-of-the-art AI • Advancing open research • Setting new standards",
            font_size=18,
            color=ACCENT_GREEN
        )
        future_text.next_to(future_title, DOWN, buff=0.4)
        
        self.play(FadeIn(future_title))
        self.play(Write(future_text))
        self.wait(2)
        
        # Meta branding
        meta_logo_text = Text("Meta AI", font_size=32, color=META_BLUE, weight=BOLD)
        meta_logo_text.move_to(RIGHT * 5 + DOWN * 3.5)
        
        self.play(FadeIn(meta_logo_text, scale=0.5))
        self.wait(2)
        
        # Final cleanup
        conclusion_elements = VGroup(
            conclusion_title, innovations_title, innovation_items,
            future_title, future_text, meta_logo_text
        )
        self.play(FadeOut(conclusion_elements))
        self.wait(1)

if __name__ == "__main__":
    """
    Configuration and execution for high-quality animation rendering.
    Optimized for production use and distribution.
    """
    config.quality = "high_quality"
    config.preview = True
    config.disable_caching = False
    config.output_file = "llama3_animation"
    
    scene = LlamaThreeAnimation()
    scene.render()
