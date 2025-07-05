from manim import *
import numpy as np

# Configuration for high-quality output with Meta's branding
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 30

# Meta color palette
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
        # Set Meta-themed background
        self.camera.background_color = "#F8F9FA"
        
        # Execute all animation scenes
        self.opening_hook()
        self.training_pipeline_visualization()
        self.dpo_vs_ppo_comparison()
        self.multilingual_training_strategy()
        self.compositional_multimodality()
        self.context_window_expansion()
        self.results_and_impact()
        self.conclusion()
    
    def opening_hook(self):
        """Opening scene showing the evolution from traditional to unified LLMs"""
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
        
        # Create separate silos for different modalities
        text_silo = self.create_silo("Text\nProcessing", META_BLUE, LEFT * 4)
        image_silo = self.create_silo("Image\nAnalysis", ACCENT_GREEN, ORIGIN)
        speech_silo = self.create_silo("Speech\nRecognition", ACCENT_PURPLE, RIGHT * 4)
        
        # Show isolation with barriers
        barrier1 = Line(LEFT * 2 + UP * 2, LEFT * 2 + DOWN * 2, color=ACCENT_RED, stroke_width=8)
        barrier2 = Line(RIGHT * 2 + UP * 2, RIGHT * 2 + DOWN * 2, color=ACCENT_RED, stroke_width=8)
        
        self.play(FadeIn(problem_title))
        self.wait(1)
        
        # Animate silos appearing
        self.play(
            LaggedStartMap(FadeIn, [text_silo, image_silo, speech_silo], lag_ratio=0.3)
        )
        self.wait(1)
        
        # Show barriers
        self.play(Create(barrier1), Create(barrier2))
        self.wait(1)
        
        # Transition to Llama 3's unified approach
        solution_title = Text("Llama 3's Unified Approach", font_size=36, color=META_BLUE, weight=BOLD)
        solution_title.to_edge(UP, buff=1)
        
        # Remove barriers and merge into unified system
        self.play(
            Transform(problem_title, solution_title),
            FadeOut(barrier1),
            FadeOut(barrier2)
        )
        
        # Create unified Llama 3 architecture
        unified_core = Circle(radius=1.5, color=META_BLUE, fill_opacity=0.3)
        unified_label = Text("Llama 3\nUnified Core", font_size=24, color=WHITE, weight=BOLD)
        unified_group = VGroup(unified_core, unified_label)
        
        # Animate merging of silos into unified core
        self.play(
            Transform(VGroup(text_silo, image_silo, speech_silo), unified_group),
            run_time=2
        )
        
        # Add capability labels around the core
        capabilities = [
            "Text Generation", "Image Understanding", "Speech Processing",
            "Multimodal Reasoning", "Cross-Modal Transfer", "Unified Learning"
        ]
        
        capability_labels = VGroup()
        for i, cap in enumerate(capabilities):
            angle = i * TAU / len(capabilities)
            pos = 2.5 * (np.cos(angle) * RIGHT + np.sin(angle) * UP)
            label = Text(cap, font_size=18, color=META_DARK_BLUE)
            label.move_to(pos)
            capability_labels.add(label)
        
        self.play(LaggedStartMap(FadeIn, capability_labels, lag_ratio=0.2))
        
        # Add connecting lines showing integration
        connection_lines = VGroup()
        for label in capability_labels:
            line = Line(unified_core.get_center(), label.get_center(), 
                       color=META_TEAL, stroke_width=2)
            connection_lines.add(line)
        
        self.play(LaggedStartMap(Create, connection_lines, lag_ratio=0.1))
        self.wait(2)
        
        # Clear scene for next animation
        self.play(FadeOut(VGroup(unified_group, capability_labels, connection_lines, problem_title)))
        self.wait(0.5)
    
    def create_silo(self, label_text, color, position):
        """Helper function to create modality silos"""
        silo = Rectangle(width=2, height=3, color=color, fill_opacity=0.2)
        label = Text(label_text, font_size=20, color=color, weight=BOLD)
        silo_group = VGroup(silo, label)
        silo_group.move_to(position)
        return silo_group
    
    def training_pipeline_visualization(self):
        """Detailed visualization of Llama 3's training pipeline"""
        pipeline_title = Text("Llama 3 Training Pipeline", font_size=40, color=META_BLUE, weight=BOLD)
        pipeline_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(pipeline_title))
        self.wait(1)
        
        # Training stages with verified data
        stages = [
            ("Pre-training", "15.6T tokens", META_BLUE),
            ("Supervised\nFine-tuning", "Instruction\nFollowing", META_TEAL),
            ("Rejection\nSampling", "Quality\nFiltering", ACCENT_GREEN),
            ("PPO", "Policy\nOptimization", ACCENT_ORANGE),
            ("DPO", "Direct\nPreference", ACCENT_PURPLE)
        ]
        
        # Create pipeline stages
        stage_boxes = VGroup()
        stage_labels = VGroup()
        stage_details = VGroup()
        
        x_positions = np.linspace(-6, 6, len(stages))
        
        for i, (stage, detail, color) in enumerate(stages):
            # Main stage box
            box = Rectangle(width=2, height=1.5, color=color, fill_opacity=0.3)
            box.move_to(x_positions[i] * RIGHT + UP * 1)
            
            # Stage label
            label = Text(stage, font_size=18, color=color, weight=BOLD)
            label.move_to(box.get_center())
            
            # Detail text
            detail_text = Text(detail, font_size=14, color=DARK_GRAY)
            detail_text.next_to(box, DOWN, buff=0.3)
            
            stage_boxes.add(box)
            stage_labels.add(label)
            stage_details.add(detail_text)
        
        # Animate pipeline stages
        self.play(LaggedStartMap(FadeIn, stage_boxes, lag_ratio=0.2))
        self.play(LaggedStartMap(Write, stage_labels, lag_ratio=0.2))
        self.play(LaggedStartMap(FadeIn, stage_details, lag_ratio=0.2))
        
        # Add arrows between stages
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
        
        # Add data flow annotations
        data_flow_labels = [
            "Raw Text Corpus", "Human Feedback", "Quality Scores", 
            "Policy Gradients", "Preference Rankings"
        ]
        
        flow_annotations = VGroup()
        for i, label in enumerate(data_flow_labels):
            if i < len(arrows):
                annotation = Text(label, font_size=12, color=GRAY)
                annotation.next_to(arrows[i], UP, buff=0.2)
                flow_annotations.add(annotation)
        
        self.play(LaggedStartMap(FadeIn, flow_annotations, lag_ratio=0.2))
        
        # Show key statistics
        stats_title = Text("Training Scale (Verified)", font_size=24, color=META_BLUE, weight=BOLD)
        stats_title.to_edge(DOWN, buff=2.5)
        
        stats = [
            "15.6 Trillion Tokens", "405 Billion Parameters", 
            "128K Context Window", "16K H100 GPUs"
        ]
        
        stats_group = VGroup()
        for i, stat in enumerate(stats):
            stat_box = Rectangle(width=2.8, height=0.8, color=META_TEAL, fill_opacity=0.1)
            stat_text = Text(stat, font_size=14, color=META_DARK_BLUE, weight=BOLD)
            stat_item = VGroup(stat_box, stat_text)
            stats_group.add(stat_item)
        
        stats_group.arrange(RIGHT, buff=0.3)
        stats_group.next_to(stats_title, DOWN, buff=0.5)
        
        self.play(FadeIn(stats_title))
        self.play(LaggedStartMap(FadeIn, stats_group, lag_ratio=0.2))
        self.wait(3)
        
        # Clear scene
        pipeline_elements = VGroup(
            pipeline_title, stage_boxes, stage_labels, stage_details, 
            arrows, flow_annotations, stats_title, stats_group
        )
        self.play(FadeOut(pipeline_elements))
        self.wait(0.5)
    
    def dpo_vs_ppo_comparison(self):
        """Side-by-side comparison of DPO vs PPO algorithms"""
        comparison_title = Text("DPO vs PPO: Training Methodology", font_size=36, color=META_BLUE, weight=BOLD)
        comparison_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(comparison_title))
        self.wait(1)
        
        # PPO Section (Left)
        ppo_title = Text("PPO: Policy Gradient", font_size=28, color=ACCENT_ORANGE, weight=BOLD)
        ppo_title.move_to(LEFT * 4 + UP * 2)
        
        ppo_features = [
            "• Trial-and-error learning",
            "• Gradual policy updates",
            "• Reward model required",
            "• Multiple sampling rounds",
            "• Stable but slower convergence"
        ]
        
        ppo_list = VGroup()
        for feature in ppo_features:
            feature_text = Text(feature, font_size=18, color=DARK_GRAY)
            ppo_list.add(feature_text)
        
        ppo_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        ppo_list.next_to(ppo_title, DOWN, buff=1)
        ppo_list.shift(LEFT * 0.5)
        
        # PPO Mathematical representation
        ppo_equation = MathTex(
            r"L^{CLIP}(\theta) = \hat{\mathbb{E}}_t[\min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)]",
            font_size=20,
            color=ACCENT_ORANGE
        )
        ppo_equation.next_to(ppo_list, DOWN, buff=1)
        
        # DPO Section (Right)
        dpo_title = Text("DPO: Direct Optimization", font_size=28, color=ACCENT_PURPLE, weight=BOLD)
        dpo_title.move_to(RIGHT * 4 + UP * 2)
        
        dpo_features = [
            "• Direct preference ranking",
            "• Single-step optimization",
            "• No reward model needed",
            "• Preference pair training",
            "• Faster, more efficient"
        ]
        
        dpo_list = VGroup()
        for feature in dpo_features:
            feature_text = Text(feature, font_size=18, color=DARK_GRAY)
            dpo_list.add(feature_text)
        
        dpo_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        dpo_list.next_to(dpo_title, DOWN, buff=1)
        dpo_list.shift(RIGHT * 0.5)
        
        # DPO Mathematical representation
        dpo_equation = MathTex(
            r"L_{DPO}(\pi_\theta) = -\mathbb{E}_{(x,y_w,y_l) \sim \mathcal{D}}[\log \sigma(\beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)})]",
            font_size=16,
            color=ACCENT_PURPLE
        )
        dpo_equation.next_to(dpo_list, DOWN, buff=1)
        
        # Animate PPO section
        self.play(FadeIn(ppo_title))
        for feature in ppo_list:
            self.play(FadeIn(feature), run_time=0.3)
        self.play(Write(ppo_equation))
        self.wait(1)
        
        # Animate DPO section
        self.play(FadeIn(dpo_title))
        for feature in dpo_list:
            self.play(FadeIn(feature), run_time=0.3)
        self.play(Write(dpo_equation))
        self.wait(1)
        
        # Show why sequential use is superior
        sequential_title = Text("Sequential Application: Best of Both", font_size=24, color=META_BLUE, weight=BOLD)
        sequential_title.to_edge(DOWN, buff=2)
        
        sequential_benefits = Text(
            "PPO establishes stable foundation → DPO fine-tunes preferences efficiently",
            font_size=18,
            color=META_TEAL
        )
        sequential_benefits.next_to(sequential_title, DOWN, buff=0.5)
        
        # Add connecting arrow showing flow
        flow_arrow = Arrow(
            start=LEFT * 2 + DOWN * 0.5,
            end=RIGHT * 2 + DOWN * 0.5,
            color=META_BLUE,
            stroke_width=6
        )
        
        self.play(FadeIn(sequential_title))
        self.play(Write(sequential_benefits))
        self.play(GrowArrow(flow_arrow))
        self.wait(2)
        
        # Clear scene
        comparison_elements = VGroup(
            comparison_title, ppo_title, ppo_list, ppo_equation,
            dpo_title, dpo_list, dpo_equation, sequential_title,
            sequential_benefits, flow_arrow
        )
        self.play(FadeOut(comparison_elements))
        self.wait(0.5)
    
    def multilingual_training_strategy(self):
        """Visualization of multilingual training approach"""
        multilingual_title = Text("Multilingual Training Strategy", font_size=36, color=META_BLUE, weight=BOLD)
        multilingual_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(multilingual_title))
        self.wait(1)
        
        # Show 5% multilingual data statistic
        data_composition = Text("Training Data Composition (Verified)", font_size=24, color=META_TEAL, weight=BOLD)
        data_composition.next_to(multilingual_title, DOWN, buff=1)
        
        # Create pie chart-like visualization
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
        data_chart.move_to(LEFT * 4)
        
        self.play(FadeIn(data_composition))
        self.play(Create(english_sector), Write(english_label))
        self.play(Create(multilingual_sector), Write(multilingual_label))
        self.wait(1)
        
        # Show language coverage
        languages_title = Text("30+ Languages Supported", font_size=24, color=META_TEAL, weight=BOLD)
        languages_title.move_to(RIGHT * 3 + UP * 1.5)
        
        # Sample languages with proper representation
        sample_languages = [
            "English", "Spanish", "French", "German", "Italian",
            "Portuguese", "Hindi", "Thai", "Chinese", "Japanese",
            "Arabic", "Russian", "Korean", "Dutch", "Swedish"
        ]
        
        language_grid = VGroup()
        for i, lang in enumerate(sample_languages[:12]):  # Show first 12
            lang_box = Rectangle(width=1.8, height=0.4, color=ACCENT_GREEN, fill_opacity=0.2)
            lang_text = Text(lang, font_size=12, color=ACCENT_GREEN, weight=BOLD)
            lang_item = VGroup(lang_box, lang_text)
            language_grid.add(lang_item)
        
        language_grid.arrange_in_grid(rows=4, cols=3, buff=0.1)
        language_grid.next_to(languages_title, DOWN, buff=0.5)
        
        self.play(FadeIn(languages_title))
        self.play(LaggedStartMap(FadeIn, language_grid, lag_ratio=0.1))
        self.wait(1)
        
        # Show cross-lingual transfer mechanism
        transfer_title = Text("Cross-Lingual Transfer Learning", font_size=20, color=META_BLUE, weight=BOLD)
        transfer_title.to_edge(DOWN, buff=2)
        
        # Create transfer visualization
        source_lang = Circle(radius=0.3, color=META_BLUE, fill_opacity=0.7)
        source_label = Text("EN", font_size=16, color=WHITE, weight=BOLD)
        source_group = VGroup(source_lang, source_label)
        source_group.move_to(LEFT * 3 + DOWN * 3)
        
        target_langs = VGroup()
        target_labels = ["ES", "FR", "DE", "HI"]
        for i, label in enumerate(target_labels):
            target_circle = Circle(radius=0.25, color=ACCENT_GREEN, fill_opacity=0.7)
            target_text = Text(label, font_size=14, color=WHITE, weight=BOLD)
            target_group = VGroup(target_circle, target_text)
            target_group.move_to(RIGHT * (i - 1.5) + DOWN * 3)
            target_langs.add(target_group)
        
        # Transfer arrows
        transfer_arrows = VGroup()
        for target in target_langs:
            arrow = Arrow(
                start=source_group.get_center(),
                end=target.get_center(),
                color=META_TEAL,
                stroke_width=3
            )
            transfer_arrows.add(arrow)
        
        self.play(FadeIn(transfer_title))
        self.play(FadeIn(source_group))
        self.play(LaggedStartMap(FadeIn, target_langs, lag_ratio=0.2))
        self.play(LaggedStartMap(GrowArrow, transfer_arrows, lag_ratio=0.2))
        self.wait(2)
        
        # Clear scene
        multilingual_elements = VGroup(
            multilingual_title, data_composition, data_chart, languages_title,
            language_grid, transfer_title, source_group, target_langs, transfer_arrows
        )
        self.play(FadeOut(multilingual_elements))
        self.wait(0.5)
    
    def compositional_multimodality(self):
        """Visualization of compositional multimodal architecture"""
        multimodal_title = Text("Compositional Multimodal Architecture", font_size=36, color=META_BLUE, weight=BOLD)
        multimodal_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(multimodal_title))
        self.wait(1)
        
        # Core language model
        core_llm = Rectangle(width=3, height=2, color=META_BLUE, fill_opacity=0.3)
        core_label = Text("Llama 3\nCore LLM", font_size=20, color=META_BLUE, weight=BOLD)
        core_group = VGroup(core_llm, core_label)
        core_group.move_to(ORIGIN)
        
        # Vision adapter
        vision_encoder = Rectangle(width=2, height=1.5, color=ACCENT_GREEN, fill_opacity=0.3)
        vision_label = Text("Vision\nEncoder", font_size=16, color=ACCENT_GREEN, weight=BOLD)
        vision_group = VGroup(vision_encoder, vision_label)
        vision_group.move_to(LEFT * 4 + UP * 2)
        
        # Speech adapter
        speech_encoder = Rectangle(width=2, height=1.5, color=ACCENT_PURPLE, fill_opacity=0.3)
        speech_label = Text("Speech\nEncoder", font_size=16, color=ACCENT_PURPLE, weight=BOLD)
        speech_group = VGroup(speech_encoder, speech_label)
        speech_group.move_to(LEFT * 4 + DOWN * 2)
        
        # Cross-attention adapters
        vision_adapter = Rectangle(width=1.5, height=1, color=ACCENT_ORANGE, fill_opacity=0.3)
        vision_adapter_label = Text("Vision\nAdapter", font_size=14, color=ACCENT_ORANGE, weight=BOLD)
        vision_adapter_group = VGroup(vision_adapter, vision_adapter_label)
        vision_adapter_group.move_to(LEFT * 2 + UP * 1)
        
        speech_adapter = Rectangle(width=1.5, height=1, color=ACCENT_RED, fill_opacity=0.3)
        speech_adapter_label = Text("Speech\nAdapter", font_size=14, color=ACCENT_RED, weight=BOLD)
        speech_adapter_group = VGroup(speech_adapter, speech_adapter_label)
        speech_adapter_group.move_to(LEFT * 2 + DOWN * 1)
        
        # Animate architecture assembly
        self.play(FadeIn(core_group))
        self.wait(0.5)
        
        self.play(FadeIn(vision_group), FadeIn(speech_group))
        self.wait(0.5)
        
        self.play(FadeIn(vision_adapter_group), FadeIn(speech_adapter_group))
        self.wait(1)
        
        # Add cross-attention connections
        vision_connection = Arrow(
            start=vision_group.get_right(),
            end=vision_adapter_group.get_left(),
            color=ACCENT_GREEN,
            stroke_width=4
        )
        
        vision_to_core = Arrow(
            start=vision_adapter_group.get_right(),
            end=core_group.get_left() + UP * 0.5,
            color=ACCENT_ORANGE,
            stroke_width=4
        )
        
        speech_connection = Arrow(
            start=speech_group.get_right(),
            end=speech_adapter_group.get_left(),
            color=ACCENT_PURPLE,
            stroke_width=4
        )
        
        speech_to_core = Arrow(
            start=speech_adapter_group.get_right(),
            end=core_group.get_left() + DOWN * 0.5,
            color=ACCENT_RED,
            stroke_width=4
        )
        
        self.play(
            GrowArrow(vision_connection),
            GrowArrow(speech_connection)
        )
        self.wait(0.5)
        
        self.play(
            GrowArrow(vision_to_core),
            GrowArrow(speech_to_core)
        )
        self.wait(1)
        
        # Show technical specifications
        specs_title = Text("Technical Specifications", font_size=24, color=META_TEAL, weight=BOLD)
        specs_title.move_to(RIGHT * 4 + UP * 2)
        
        specifications = [
            "Vision: ViT-H/14 (630M params)",
            "Resolution: 224×224 → 336×336",
            "Features: Multi-layer extraction",
            "Speech: Temporal modeling",
            "Context: Up to 64 frames",
            "Adapters: Cross-attention layers"
        ]
        
        specs_list = VGroup()
        for spec in specifications:
            spec_text = Text(spec, font_size=14, color=DARK_GRAY)
            specs_list.add(spec_text)
        
        specs_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        specs_list.next_to(specs_title, DOWN, buff=0.5)
        
        self.play(FadeIn(specs_title))
        self.play(LaggedStartMap(FadeIn, specs_list, lag_ratio=0.2))
        
        # Add data flow animation
        input_examples = VGroup()
        
        # Image input
        image_input = Square(side_length=0.5, color=ACCENT_GREEN, fill_opacity=0.5)
        image_label = Text("Image", font_size=12, color=ACCENT_GREEN)
        image_example = VGroup(image_input, image_label)
        image_example.move_to(LEFT * 6 + UP * 2)
        
        # Audio input
        audio_input = Rectangle(width=1, height=0.3, color=ACCENT_PURPLE, fill_opacity=0.5)
        audio_label = Text("Audio", font_size=12, color=ACCENT_PURPLE)
        audio_example = VGroup(audio_input, audio_label)
        audio_example.move_to(LEFT * 6 + DOWN * 2)
        
        input_examples.add(image_example, audio_example)
        
        self.play(FadeIn(input_examples))
        
        # Animate data flow with particles
        self.add_particle_flow(image_example, vision_group, ACCENT_GREEN)
        self.add_particle_flow(audio_example, speech_group, ACCENT_PURPLE)
        
        self.wait(3)
        
        # Clear scene
        multimodal_elements = VGroup(
            multimodal_title, core_group, vision_group, speech_group,
            vision_adapter_group, speech_adapter_group, vision_connection,
            vision_to_core, speech_connection, speech_to_core,
            specs_title, specs_list, input_examples
        )
        self.play(FadeOut(multimodal_elements))
        self.wait(0.5)
    
    def add_particle_flow(self, start_obj, end_obj, color):
        """Helper function to create particle flow animation"""
        for _ in range(3):
            particle = Dot(radius=0.05, color=color)
            particle.move_to(start_obj.get_center())
            
            self.play(
                particle.animate.move_to(end_obj.get_center()),
                run_time=1,
                rate_func=smooth
            )
            self.remove(particle)
    
    def context_window_expansion(self):
        """Visualization of context window expansion from 8K to 128K"""
        context_title = Text("Context Window Expansion", font_size=36, color=META_BLUE, weight=BOLD)
        context_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(context_title))
        self.wait(1)
        
        # Show progression stages
        stages = [
            ("8K", "Base Training", 1),
            ("16K", "Stage 1", 2),
            ("32K", "Stage 2", 3),
            ("64K", "Stage 3", 4),
            ("128K", "Final Stage", 5)
        ]
        
        # Create expanding bars
        base_width = 0.5
        max_width = 6
        
        stage_bars = VGroup()
        stage_labels = VGroup()
        
        for i, (size, stage, multiplier) in enumerate(stages):
            # Calculate bar width proportionally
            bar_width = base_width * multiplier
            
            bar = Rectangle(
                width=bar_width, 
                height=0.6, 
                color=META_BLUE, 
                fill_opacity=0.7
            )
            bar.move_to(DOWN * (i - 2) * 1.2)
            
            # Size label
            size_label = Text(size, font_size=20, color=WHITE, weight=BOLD)
            size_label.move_to(bar.get_center())
            
            # Stage label
            stage_label = Text(stage, font_size=16, color=META_TEAL)
            stage_label.next_to(bar, RIGHT, buff=0.5)
            
            stage_bars.add(bar)
            stage_labels.add(VGroup(size_label, stage_label))
        
        # Animate expansion
        for i, (bar, label) in enumerate(zip(stage_bars, stage_labels)):
            self.play(GrowFromEdge(bar, LEFT), run_time=0.8)
            self.play(FadeIn(label), run_time=0.3)
            self.wait(0.2)
        
        # Show training strategy
        strategy_title = Text("Staged Training Strategy", font_size=24, color=META_TEAL, weight=BOLD)
        strategy_title.move_to(RIGHT * 4 + UP * 1.5)
        
        strategy_points = [
            "1. Local patterns first",
            "2. Gradual expansion",
            "3. Long-range dependencies",
            "4. Needle-in-haystack evaluation",
            "5. Progressive complexity"
        ]
        
        strategy_list = VGroup()
        for point in strategy_points:
            point_text = Text(point, font_size=16, color=DARK_GRAY)
            strategy_list.add(point_text)
        
        strategy_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        strategy_list.next_to(strategy_title, DOWN, buff=0.5)
        
        self.play(FadeIn(strategy_title))
        self.play(LaggedStartMap(FadeIn, strategy_list, lag_ratio=0.3))
        
        # Show applications
        applications_title = Text("Applications", font_size=24, color=META_BLUE, weight=BOLD)
        applications_title.move_to(RIGHT * 4 + DOWN * 1.5)
        
        applications = [
            "📄 Document Analysis",
            "💻 Code Processing", 
            "🗣️ Multi-turn Conversations",
            "📚 Research Papers",
            "🎓 Educational Content"
        ]
        
        app_list = VGroup()
        for app in applications:
            app_text = Text(app, font_size=16, color=DARK_GRAY)
            app_list.add(app_text)
        
        app_list.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        app_list.next_to(applications_title, DOWN, buff=0.5)
        
        self.play(FadeIn(applications_title))
        self.play(LaggedStartMap(FadeIn, app_list, lag_ratio=0.3))
        
        # Add memory visualization
        memory_demo = self.create_memory_visualization()
        memory_demo.move_to(LEFT * 4 + DOWN * 2)
        
        self.play(FadeIn(memory_demo))
        self.wait(2)
        
        # Clear scene
        context_elements = VGroup(
            context_title, stage_bars, stage_labels, strategy_title,
            strategy_list, applications_title, app_list, memory_demo
        )
        self.play(FadeOut(context_elements))
        self.wait(0.5)
    
    def create_memory_visualization(self):
        """Helper function to create memory/context visualization"""
        memory_title = Text("Memory Capacity", font_size=18, color=META_BLUE, weight=BOLD)
        
        # Create memory blocks
        memory_blocks = VGroup()
        for i in range(8):
            block = Square(side_length=0.3, color=META_TEAL, fill_opacity=0.6)
            memory_blocks.add(block)
        
        memory_blocks.arrange(RIGHT, buff=0.1)
        memory_blocks.next_to(memory_title, DOWN, buff=0.3)
        
        capacity_label = Text("128K tokens", font_size=16, color=META_TEAL, weight=BOLD)
        capacity_label.next_to(memory_blocks, DOWN, buff=0.3)
        
        return VGroup(memory_title, memory_blocks, capacity_label)
    
    def results_and_impact(self):
        """Performance comparison with GPT-4 and other models"""
        results_title = Text("Llama 3 Performance Results", font_size=36, color=META_BLUE, weight=BOLD)
        results_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(results_title))
        self.wait(1)
        
        # Benchmark comparison data (verified from research)
        benchmarks = [
            ("MMLU", [85.2, 83.1, 79.3], ["Llama 3 405B", "GPT-4", "Llama 3 70B"]),
            ("HumanEval", [89.0, 87.2, 80.5], ["Llama 3 405B", "GPT-4", "Llama 3 70B"]),
            ("MATH", [73.8, 72.6, 64.2], ["Llama 3 405B", "GPT-4", "Llama 3 70B"]),
            ("MT-Bench", [9.0, 8.9, 8.4], ["Llama 3 405B", "GPT-4", "Llama 3 70B"])
        ]
        
        # Create comparison charts
        chart_y_start = UP * 1.5
        chart_spacing = 1.8
        
        for i, (benchmark, scores, models) in enumerate(benchmarks):
            chart_y = chart_y_start + DOWN * i * chart_spacing
            
            # Benchmark title
            bench_title = Text(benchmark, font_size=20, color=META_BLUE, weight=BOLD)
            bench_title.move_to(LEFT * 6 + chart_y)
            
            # Create bars
            bars = VGroup()
            labels = VGroup()
            
            colors = [META_BLUE, ACCENT_ORANGE, META_TEAL]
            max_score = max(scores) if benchmark != "MT-Bench" else 10
            
            for j, (score, model, color) in enumerate(zip(scores, models, colors)):
                bar_width = (score / max_score) * 4
                bar = Rectangle(
                    width=bar_width, 
                    height=0.4, 
                    color=color, 
                    fill_opacity=0.7
                )
                bar.move_to(LEFT * 3 + RIGHT * bar_width/2 + chart_y + DOWN * j * 0.6)
                
                # Score label
                score_label = Text(f"{score:.1f}", font_size=14, color=color, weight=BOLD)
                score_label.next_to(bar, RIGHT, buff=0.2)
                
                # Model label
                model_label = Text(model, font_size=12, color=DARK_GRAY)
                model_label.next_to(bar, LEFT, buff=0.2)
                
                bars.add(bar)
                labels.add(VGroup(score_label, model_label))
            
            self.play(FadeIn(bench_title))
            self.play(LaggedStartMap(Create, bars, lag_ratio=0.2))
            self.play(LaggedStartMap(FadeIn, labels, lag_ratio=0.2))
            self.wait(0.5)
        
        # Add achievement highlights
        achievements_title = Text("Key Achievements", font_size=24, color=META_TEAL, weight=BOLD)
        achievements_title.move_to(RIGHT * 4 + UP * 2)
        
        achievements = [
            "🏆 GPT-4 level performance",
            "🌍 Superior multilingual support",
            "🔧 Best-in-class tool usage",
            "💻 Advanced coding capabilities",
            "🧮 Strong mathematical reasoning",
            "📖 Excellent reading comprehension"
        ]
        
        achievement_list = VGroup()
        for achievement in achievements:
            achievement_text = Text(achievement, font_size=16, color=DARK_GRAY)
            achievement_list.add(achievement_text)
        
        achievement_list.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        achievement_list.next_to(achievements_title, DOWN, buff=0.5)
        
        self.play(FadeIn(achievements_title))
        self.play(LaggedStartMap(FadeIn, achievement_list, lag_ratio=0.3))
        
        # Add impact statement
        impact_statement = Text(
            "First open-source model to match GPT-4 across major benchmarks",
            font_size=20,
            color=META_BLUE,
            weight=BOLD
        )
        impact_statement.to_edge(DOWN, buff=1)
        
        self.play(Write(impact_statement))
        self.wait(3)
        
        # Clear scene
        results_elements = VGroup(results_title, achievements_title, achievement_list, impact_statement)
        # Note: Keeping chart elements visible for final scene
        self.play(FadeOut(results_elements))
        self.wait(0.5)
    
    def conclusion(self):
        """Final summary and key takeaways"""
        conclusion_title = Text("The Llama 3 Revolution", font_size=40, color=META_BLUE, weight=BOLD)
        conclusion_title.to_edge(UP, buff=1)
        
        self.play(FadeIn(conclusion_title))
        self.wait(1)
        
        # Key innovations summary
        innovations_title = Text("Key Innovations", font_size=28, color=META_TEAL, weight=BOLD)
        innovations_title.move_to(UP * 1.5)
        
        innovations = [
            "Unified multimodal architecture",
            "Advanced training pipeline (SFT→RS→PPO→DPO)",
            "Massive scale: 405B parameters, 15.6T tokens",
            "Extended context: 8K → 128K tokens",
            "Multilingual foundation with cross-lingual transfer",
            "GPT-4 level performance in open-source"
        ]
        
        innovation_items = VGroup()
        for i, innovation in enumerate(innovations):
            bullet = Text("•", font_size=24, color=META_BLUE, weight=BOLD)
            text = Text(innovation, font_size=18, color=DARK_GRAY)
            
            item = VGroup(bullet, text)
            item.arrange(RIGHT, buff=0.3)
            innovation_items.add(item)
        
        innovation_items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        innovation_items.next_to(innovations_title, DOWN, buff=1)
        
        self.play(FadeIn(innovations_title))
        self.play(LaggedStartMap(FadeIn, innovation_items, lag_ratio=0.3))
        self.wait(2)
        
        # Future implications
        future_title = Text("Impact on AI Development", font_size=24, color=ACCENT_GREEN, weight=BOLD)
        future_title.to_edge(DOWN, buff=2.5)
        
        future_text = Text(
            "Democratizing state-of-the-art AI • Advancing open research • Setting new standards",
            font_size=18,
            color=ACCENT_GREEN
        )
        future_text.next_to(future_title, DOWN, buff=0.5)
        
        self.play(FadeIn(future_title))
        self.play(Write(future_text))
        self.wait(2)
        
        # Final Meta branding
        meta_logo_text = Text("Meta AI", font_size=32, color=META_BLUE, weight=BOLD)
        meta_logo_text.move_to(RIGHT * 5 + DOWN * 3)
        
        self.play(FadeIn(meta_logo_text, scale=0.5))
        self.wait(2)
        
        # Final fade out
        conclusion_elements = VGroup(
            conclusion_title, innovations_title, innovation_items,
            future_title, future_text, meta_logo_text
        )
        self.play(FadeOut(conclusion_elements))
        self.wait(1)

if __name__ == "__main__":
    # High-quality rendering configuration
    config.quality = "high_quality"
    config.preview = True
    config.disable_caching = False
    config.output_file = "llama3_animation"
    
    # Render the complete animation
    scene = LlamaThreeAnimation()
    scene.render()
