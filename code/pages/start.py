import pygame
from settings import *
from button import Button
from pages.koa import Koa

class Start:
    def __init__(self):
        pygame.init()

        # Set up the game window
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Studemon")

        self.running = True
        self.clock = pygame.time.Clock()

        # Text attributes
        self.font = pygame.font.Font(None, 36)
        self.text_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)
        self.box_color_inactive = (200, 200, 200)
        self.box_color_active = (255, 255, 255)

        # Data storage for questions and answers
        self.questions = []
        self.answers = []

        # Current input fields
        self.current_question = ""
        self.current_answer = ""

        # Active input field (0 = question, 1 = answer)
        self.active_input = 0

        # Input box dimensions
        self.question_box = pygame.Rect(50, 160, 400, 40)  # x, y, width, height
        self.answer_box = pygame.Rect(WINDOW_WIDTH // 2 + 50, 160, 400, 40)
        
        # Feedback message
        self.show_feedback = False
        self.feedback_message = ""
        self.feedback_timer = 0
        self.feedback_duration = 2000  # Display feedback for 2 seconds

    def run(self):
        """ Main game loop """
        while self.running:
            # Control frame rate
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # Handle key inputs
                    if event.key == pygame.K_RETURN:
                        # Save current question and answer
                        if self.current_question and self.current_answer:
                            self.questions.append(self.current_question)
                            self.answers.append(self.current_answer)
                            self.current_question = ""
                            self.current_answer = ""
                            self.active_input = 0  # Reset to question input
                            # Show success message
                            self.show_feedback = True
                            self.feedback_message = "Q&A pair added successfully!"
                            self.feedback_timer = pygame.time.get_ticks()
                        else:
                            # Show error message if either field is empty
                            self.show_feedback = True
                            self.feedback_message = "Both question and answer are required!"
                            self.feedback_timer = pygame.time.get_ticks()
                    elif event.key == pygame.K_TAB:
                        # Switch input field
                        self.active_input = (self.active_input + 1) % 2
                    elif event.key == pygame.K_BACKSPACE:
                        # Remove last character from the active input
                        if self.active_input == 0:
                            self.current_question = self.current_question[:-1]
                        elif self.active_input == 1:
                            self.current_answer = self.current_answer[:-1]
                    else:
                        # Add typed character to the active input
                        if self.active_input == 0:
                            self.current_question += event.unicode
                        elif self.active_input == 1:
                            self.current_answer += event.unicode

            # Draw the screen
            self.window.fill(self.bg_color)

            # Background image
            bg = pygame.image.load("images/other/startscreen.png")
            next_img = pygame.image.load("images/buttons/next.png").convert_alpha()
            next_button = Button("next", WINDOW_WIDTH - 300, 0, next_img, 6)

            self.window.blit(bg, (0, 0))
            
            # Only proceed if we have at least one Q&A pair
            if next_button.draw(self.window) and len(self.questions) > 0:
                data = {}
                for i in range(len(self.questions)):
                    data[self.questions[i]] = self.answers[i]
                
                koa = Koa(data)
                koa.run()
            # If next is clicked but no Q&A pairs exist, show feedback
            elif next_button.draw(self.window) and len(self.questions) == 0:
                self.show_feedback = True
                self.feedback_message = "Please add at least one Q&A pair before continuing!"
                self.feedback_timer = pygame.time.get_ticks()
                
            # Draw header
            self.draw_text("Make Your Study Set", 50, 20)
            self.draw_text("Type directly to input the question, press tab to start inputting the answer.", 50, 60)
            self.draw_text("Then press enter to submit the Q&A!", 50, 100)

            # Draw labels for input boxes
            self.draw_text("Question:", 50, 140)
            self.draw_text("Answer:", WINDOW_WIDTH // 2 + 50, 140)

            # Draw input boxes
            pygame.draw.rect(self.window, self.box_color_active if self.active_input == 0 else self.box_color_inactive, self.question_box)
            pygame.draw.rect(self.window, self.box_color_active if self.active_input == 1 else self.box_color_inactive, self.answer_box)

            # Draw input text inside boxes
            question_surface = self.font.render(self.current_question, True, self.text_color)
            answer_surface = self.font.render(self.current_answer, True, self.text_color)
            self.window.blit(question_surface, (self.question_box.x + 5, self.question_box.y + 5))
            self.window.blit(answer_surface, (self.answer_box.x + 5, self.answer_box.y + 5))

            # Display feedback message if needed
            if self.show_feedback:
                current_time = pygame.time.get_ticks()
                if current_time - self.feedback_timer < self.feedback_duration:
                    # Choose color based on message type (error or success)
                    if "required" in self.feedback_message or "Please add" in self.feedback_message:
                        feedback_color = (255, 0, 0)  # Red for errors
                    else:
                        feedback_color = (0, 128, 0)  # Green for success
                    
                    feedback_surface = self.font.render(self.feedback_message, True, feedback_color)
                    self.window.blit(feedback_surface, (WINDOW_WIDTH // 2 - feedback_surface.get_width() // 2, 210))
                else:
                    self.show_feedback = False

            # Draw saved question-answer pairs
            y_offset = 240  # Start below the input fields
            if len(self.questions) == 0:
                self.draw_text("No Q&A pairs added yet", 50, y_offset)
            else:
                for i in range(len(self.questions)):
                    self.draw_text(f"Q: {self.questions[i]}", 50, y_offset)
                    self.draw_text(f"A: {self.answers[i]}", WINDOW_WIDTH // 2 + 50, y_offset)
                    y_offset += 50

            # Update the display
            pygame.display.update()

        pygame.quit()

    def draw_text(self, text, x, y):
        """ Helper function to draw text on the screen """
        text_surface = self.font.render(text, True, self.text_color)
        self.window.blit(text_surface, (x, y))