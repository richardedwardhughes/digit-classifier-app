import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Drawing Mirror App 🎨")
st.write("Draw something on the canvas, then click **Flip Image** to reflect it across the vertical axis.")

# 1. Sidebar Control
st.sidebar.header("Canvas Settings")
stroke_width = st.sidebar.slider("Brush Size", min_value=5, max_value=40, value=15)

# 2. Interactive Canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",
    stroke_width=stroke_width,
    stroke_color="#FFFFFF",
    background_color="#000000",
    height=280,
    width=280,
    drawing_mode="freedraw",
    update_streamlit=True,
    return_image_data=True,
    key="mirror_canvas",
)

# 3. Image Flipping Logic
if st.button("Flip Image", type="primary"):
    if canvas_result.image_data is not None and canvas_result.image_data.any():
        original_img = canvas_result.image_data

        # Flip horizontally (left-to-right across the vertical axis)
        flipped_img = np.fliplr(original_img)

        # Display Original and Flipped side-by-side
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Original Drawing**")
            st.image(original_img, width=200)

        with col2:
            st.write("**Flipped Drawing**")
            st.image(flipped_img, width=200)
    else:
        st.warning("Please draw something on the canvas first!")