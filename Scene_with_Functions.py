from graphics import Canvas
import math

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw three clouds
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 40, 30, 'lightblue')
    draw_cloud(canvas, 220, 50, 'white')
    
    # Draw three trees
    draw_tree(canvas, 60, 'sienna', 'forestgreen')
    draw_tree(canvas, 180, 'saddlebrown', 'darkgreen')
    draw_tree(canvas, 300, 'brown', 'limegreen')

def draw_cloud(canvas, x, y, color):
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH

    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

def draw_tree(canvas, x, trunk_color, leaves_color):
    """
    Draws a single tree with a trunk and a circle of leaves.
    The tree is placed so that the bottom of the trunk is at TREE_BOTTOM_Y.
    """
    # Draw trunk
    trunk_top_y = TREE_BOTTOM_Y - TRUNK_HEIGHT
    canvas.create_rectangle(
        x, trunk_top_y,
        x + TRUNK_WIDTH, TREE_BOTTOM_Y,
        trunk_color
    )
    
    # Draw leaves (centered above the trunk)
    leaf_center_x = x + TRUNK_WIDTH / 2
    leaf_center_y = trunk_top_y - LEAVES_SIZE / 2
    canvas.create_oval(
        leaf_center_x - LEAVES_SIZE / 2, 
        leaf_center_y - LEAVES_SIZE / 2, 
        leaf_center_x + LEAVES_SIZE / 2, 
        leaf_center_y + LEAVES_SIZE / 2, 
        leaves_color
    )

if __name__ == '__main__':
    main()
