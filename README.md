# **Day and Night Simulation of RGB and Thermal Views**

This project simulates a map with various blocks, such as trees, houses, roads, ponds, and animals. It provides two different views: an **RGB view** and a **thermal view**. The brightness and color contrast of both views change dynamically throughout a 24-hour cycle, simulating the day and night transitions.

- In the **RGB view**, the brightness starts low at hour 0 (midnight), increases to its peak at hour 12 (noon), and then decreases back to low brightness by hour 24 (midnight).
- In the **thermal view**, the color contrast changes dynamically based on temperature. The temperature is lowest in the early morning and night, and highest around noon.

## **Features**
1. **RGB View**: Changes dynamically based on the time of day, with color brightness increasing until noon and decreasing afterward.
2. **Thermal View**: Displays item-specific temperatures, with dynamic contrast changes based on the hour of the day.
3. **Map with Different Items**: Simulates a map containing trees, houses, roads, ponds, and animals, each represented with appropriate shapes and colors.

## **Simulation Map Components**
- **Trees**: Orange in thermal view, dark green in RGB view.
- **Houses**: Yellow in thermal view, brown in RGB view.
- **Animals**: Red in both views.
- **Ponds**: Blue in both views.
- **Roads**: Gray in both views.

## **Dynamic Day Simulation**
- Brightness in the **RGB view** changes based on the hour of the day.
- Temperature and contrast in the **thermal view** adjust according to the time of day, following a sinusoidal temperature curve.

## **Project Structure**

Here’s an overview of the main files in this project:

- **`cano.py`**: The main entry point that runs the simulation and generates the day cycle views.
- **`map_simulation.py`**: Defines the map and generates the RGB and thermal views.
- **`items.py`**: Contains classes that define items (trees, houses, roads, ponds, animals) and their thermal properties.
- **`blocks.py`**: Defines the blocks in the map, which are collections of items.
- **`visuals.py`**: Contains the plotting functions for RGB and thermal views.
- **`README.md`**: This file provides a detailed explanation of the project and instructions for running the simulation.

## **Customization**

- **Items on the Map**: You can modify the positions and types of items (trees, houses, animals, etc.) in the `main()` function in `cano.py`.

- **Day Simulation**: The sinusoidal brightness and temperature adjustments are defined by the following formulas:

  - **Brightness for RGB view**:

    ```python
    brightness_factor = np.sin(np.pi * hour / 24)
    ```

  - **Temperature for thermal view**:

    ```python
    temp = 10 + (15 * np.sin(np.pi * (hour - 6) / 12))
    ```

---

## **Installation Guide**

### **Prerequisites**
- Python 3.10+ is required to run this project.
- Make sure to have `pip` (Python package installer) installed.

### **Project Dependencies**
The following dependencies are required for this project:
- **`matplotlib`**: For generating and displaying plots.
- **`numpy`**: For mathematical operations, including sinusoidal calculations for brightness and temperature.

### **Steps to Install Dependencies**

1. **Install the required dependencies**:
   ```bash
   pip install matplotlib numpy
   ```

## **How to Run the Simulation**

1. **Run the simulation**.
   ```bash
   python cano.py
   ```