import gradio as gr

def process(text):
    return f"You said: {text}"

demo = gr.Interface(fn=process, inputs="text", outputs="text")
demo.launch()
