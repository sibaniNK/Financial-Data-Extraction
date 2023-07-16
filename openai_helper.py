import openai
from secret_key import openai_key
import json
import pandas as pd
openai.api_key= openai_key

# text is giving a financial paragraph
def extract_financial_data(text):
    prompt = get_prompt_financial() + text  # our instuction and the text wiil combinely give to prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content":prompt}])
    content = response.choices[0]['message']['content']  # the contect must be string in a dictionary form

    # by the help of json load the string then convert into dictionary
    try:
        data = json.loads(content)
        # here we use  return because we want to use the data frame in streamlit to display
        return pd.DataFrame(data.items(),columns=["Measure","Values"]) # data.items() used to load the row and column in pandas
    except (json.JSONDecodeError,IndexError):
        pass
    return pd.DataFrame({
        "Measure": ["Company Name","Stock Symbol","Revenue","Net Income","EPS"],
        "Values": ["", "", "", "", ""]
    })

def get_prompt_financial():
    return ''' Please retrieve company name, revenue,net income and earnings per share (a.k.a. EPS)
    from the following news article. If you can't find the information from this article then 
    return "".do not make things up.
    Then retrieve a stock symbol corresponding to that company. For this you can use 
    your general knowledge(It doesn't have to be from this article ). Always return your response as a 
    valid JSON string. the format of that string should be this ,
    {
       "Company Name : "Walmart",
       "Stock Symbol :  " WMT",
       "Revenue"      : "12.34 million ",                         
       "Net Income : "34.78 million",
       "EPS" : "2.1 $"
       
    }
    '''



if __name__ == '__main__':
    text ='''
    Tesla's Earning news in text format : Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ pofit against a revenue of 30 billion $ .
    '''


    df = extract_financial_data(text)
    print(df.to_string())