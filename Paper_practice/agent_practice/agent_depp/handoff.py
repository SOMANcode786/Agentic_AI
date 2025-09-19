from agents import Agent,Runner
from dotenv import load_dotenv


load_dotenv()


spansih_agent=Agent(
    name="Spanish Agent",
    instructions="you area spanih agent the user asked question in spasih give the answer "
)

german_agent=Agent (
    name="German Agent",
    instructions="you are  a german language agent take the aswer to the german querry"
)

triage_agent=Agent(
    name="gernal Agent",
    instructions="""
     if the user asked the gernal question aswer you .
     if the user ased quetion in spanish task delegate to spanish agent 
     if the user asked question in german task delegate to german agent 
    """,
     handoffs=[spansih_agent,german_agent]
    
)

querry=input("Enter the question : ")
result=Runner.run_sync(triage_agent,querry)

print(result.final_output)
print(result.last_agent.name)