FROM python:slim
ENV TOKEN='5706169432:AAENLIvrxYFBNV798j3b6roajYfIT_bYZMw'
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]