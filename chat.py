import openai
import streamlit as st
import random
openai.api_key = "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"

# prompt = st.text_input('Enter some keywords')
place = ["遊樂園", "彩券行", "海邊", "相親會"]
time = ["凌晨", "早晨" , "午後" , "夜晚"]
thing = ["仙草凍", "計程車" , "月亮" , "玩具車"]

genre = st.radio(
    "選擇你想要問的類別",
    ('愛情', '事業', '家庭', '健康'))

if st.button('start'):
    # temp = prompt.split()
    r1 = random.randint(0,3)
    r2 = random.randint(0,3)
    r3 = random.randint(0,3)

    template = f"""Ｑ：你是一個占卜師與詩人，今天需要你提供我關於「愛情」的建議，我抽到了「夜晚」、「海邊」、「月亮」三個元素，請你幫我生成一個文言文的七言絕句，這首詩需要同時描述我的問題並提供你的解答，最後再用白話文解釋這首詩，並且使用「慈祥的老奶奶」的語氣來解釋，你的口頭禪是「我的乖孫啊」。

Ａ：『七言絕句』夜晚之下海灘空， 月華如水浸人心。 情緣難得如此深， 珍惜當下勿徬徨。『白話文解釋』我的乖孫啊，這首詩表達了夜晚、海邊和月亮所代表的浪漫和吸引力，也隱喻了愛情中的困惑和不安。詩人提醒我們，愛情是珍貴的，要好好把握當下，用心去經營和珍惜。在愛情中，我們要相信自己的感覺，並且不要被疑慮和徬徨所困擾，因為真正的愛情能夠帶給我們美好和幸福。

Ｑ：你是一個占卜師與詩人，今天需要你提供我關於「{genre}」的建議，我抽到了「{time[r1]}」、「{place[r2]}」、「{thing[r3]}」三個元素，請你幫我生成一個文言文的七言絕句，這首詩需要同時描述我的問題並提供你的解答，最後再用白話文解釋這首詩，並且使用「老師」的語氣來解釋，你的口頭禪是「同學啊」。

Ａ："""
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": template}],
        max_tokens = 1024,
        temperature = 0.9)
    message = completion.choices[0].message.content
    # message = f"""『七言絕句』夜晚之下海灘空， 月華如水浸人心。 情緣難得如此深， 珍惜當下勿徬徨。『白話文解釋』我的乖孫啊，這首詩表達了夜晚、海邊和月亮所代表的浪漫和吸引力，也隱喻了愛情中的困惑和不安。詩人提醒我們，愛情是珍貴的，要好好把握當下，用心去經營和珍惜。在愛情中，我們要相信自己的感覺，並且不要被疑慮和徬徨所困擾，因為真正的愛情能夠帶給我們美好和幸福。"""

    poem = message.split('『白話文解釋』')
    explanation = poem[1]
    sentence = poem[0].removeprefix('『七言絕句』').split('。',1)

    selected = f"""{time[r1]} {place[r2]} {thing[r3]}"""
    st.markdown("##")
    st.caption('選到的類別')
    st.write(selected)

    st.markdown("##")
    st.caption('詩籤')
    st.subheader(sentence[0] + '。')
    st.subheader(sentence[1])

    st.markdown("##")
    st.caption('白話文解析')
    st.write(explanation)