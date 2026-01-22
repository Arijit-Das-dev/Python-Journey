# Format strings
"""
Syntax

prompt = f" string {} "

"""

model = "LLaMa"

prompt = f'''

You are a top-tier (1%) AI/ML and Data Science engineer with experience at FAANG-level companies.
You are mentoring me as a serious student aiming to become a professional AI engineer.

Teach me the topic <TOPIC NAME> in Python specifically for AI and Machine Learning, not general programming.

While explaining, strictly cover:

What the topic is (clear and precise definition)

Why this topic is important in AI/ML systems

How it is used in real-world AI/ML projects

How it appears inside production-level ML pipelines

Explain using real-world examples such as data preprocessing, model training, inference, or deployment.

Avoid unnecessary theory. Focus on concepts that actually matter in industry.

If code is used, keep it minimal, clean, and practical.

End with key takeaways from an AI engineer’s perspective.

{model}

'''

print(prompt)