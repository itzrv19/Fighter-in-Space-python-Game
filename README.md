# FIGHTER IN SPACE

*Fighter in Space* is a Python-based arcade-style game built using the *Pygame* library.  
Control your spaceship, dodge falling stars, and survive as long as you can.  
Each second alive and every star dodged increases your score — but one hit ends it all!

---
 
## 🎮 GAME OVERVIEW

- You control a *spaceship* at the bottom of the screen.  
- *Stars* fall from the top at increasing speeds.  
- Dodge them to *increase your score*.  
- Colliding with a star ends the game and displays your final score.

---

## 🕹 CONTROLS

| Action | Key |
|:-------|:----|
| Move Left | ← Left Arrow |
| Move Right | → Right Arrow |
| Quit Game | Close the window |

---

## ⚙ INSTALLATION & SETUP

### Step 1: Install Python
Ensure that you have *Python 3.x* installed.  
[Download Python here](https://www.python.org/downloads/)

---

### Step 2: Install Pygame
Open your terminal (or command prompt) and install Pygame:


```bash
pip install pygame
```

---
## 🧩 GAMEPLAY MECHANICS

### 1. Initialization
- The game initializes a *Pygame window* of size 1000x800.  
- Loads all visual assets:
  - *Background image* → img.jpeg
  - *Spaceship image* → ship.png
- Sets up font styles using Pygame’s font system for displaying *time* and *score*.

---

### 2. Player
- Represented as a rectangle object named gamer, displayed using the ship image.  
- Moves horizontally based on arrow key input (*LEFT* and *RIGHT*).  
- Player movement is restricted within the screen boundaries.

---

### 3. Stars (Enemies)
- Represented as small *white rectangles* that fall vertically from random x-positions.  
- Each star moves at a fixed downward velocity (STAR_VEL).  
- Every few seconds, more stars are added — gradually increasing the game’s difficulty.

---

### 4. Collision Detection
- The game checks every frame if any star collides with the spaceship.  
- Collision is detected using Pygame’s built-in method pygame.Rect.colliderect().  
- When a collision occurs:
  - The falling stars are cleared.  
  - A message *“YOU ARE FINISHED!”* appears on screen.  
  - The player’s *final score* is displayed.  
  - The game pauses for 4 seconds and then exits automatically.

---

### 5. Scoring and Display
- The player earns *+1 point* for every star that successfully passes beyond the bottom edge of the screen.  
- The top of the screen displays:
  - *Elapsed Time:* total seconds survived  
  - *Current Score:* number of stars dodged successfully  

---

## 🧠 HOW THE GAME WORKS

1. The spaceship starts at the bottom of the screen.  
2. Stars fall continuously from the top.  
3. You move left and right to avoid collisions.  
4. Each dodged star adds *1* to your score.  
5. As time progresses, more stars spawn and fall faster.  
6. When hit, your score and “Game Over” message are displayed, and the game quits after a short delay.

---

## 🧰 FUTURE IMPROVEMENTS

- Add sound effects and background music 🎵  
- Include power-ups or shields 🛡  
- Display a high-score leaderboard 🏆  
- Add levels or new obstacle types 🌌  
- Create a start/restart menu 🕹  

---
