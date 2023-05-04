import streamlit as st
import time
from graphviz import Digraph
from main import company, client,max_position

st.set_page_config(
    page_title='Assignment Problem',
    page_icon=('∑'),
    layout='wide',
)

st.markdown(
    """
    <style>
        .appview-container .main .block-container {
            padding-top: 30px;
        }
        .stProgress > div > div > div > div {
            background-color: red;
        }
        .stProgress {
            display: none;
        }
        p {
            text-align: center;
        }
        .stVideo {
            width: 50px;
        }
    </style>""",
    unsafe_allow_html=True,
)

if 'n_company' not in st.session_state:
    st.session_state.n_company = 1
if 'n_client' not in st.session_state:
    st.session_state.n_client = 1
if 'company_names' not in st.session_state:
    st.session_state.company_names = []
if 'clients_names' not in st.session_state:
    st.session_state.clients_names = []
if 'graph' not in st.session_state:
    st.session_state['graph']=Digraph('G')
else:
    graph = st.session_state['graph']
    st.session_state['graph'].clear()

col1,col2,col3=st.columns([1.5,0.25,3])

with col1:
    st.title(':red[Assignment Problem]')

with col2:
    with st.empty():
        ''
    with st.empty():
        ''
    button=st.button('Start',help='Start the algorithm')

with col3:
    with st.empty():
        ''
    with st.empty():
        ''
    play=st.button('▶',help='Video Explanation')

if play:
    col1_v,col2_v,col3_v= st.columns([2,0.25,2])
    with col1_v:
        video_file = open('animation.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(data=video_bytes)
        st.write(':red[Algorithm]')
    with col3_v:
        video_file = open('video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(data=video_bytes)
        st.write(':red[Application]')

my_bar = st.progress(0,text='Operation in progress...')
Tab1,Tab2=st.tabs(['Company','Client'])
companies=[]
clients=[]
choices={}

with Tab1:
    col1_tab1,col2_tab1,col3_tab1=st.columns([1.5,1,4])
    col1_but,col2_but=st.columns([0.5,8])
    st.session_state['company_names'].clear()
    for i in range(st.session_state.n_company):
        visibility='collapsed'
        if i==0:
            visibility='visible'
        with col1_tab1:
            if (st.text_input(':red[Name]',key=f'company_name{i+1}',label_visibility=visibility) 
                and st.session_state[f'company_name{i+1}'] 
                not in st.session_state['company_names']):
                st.session_state['company_names'].append(st.session_state[f'company_name{i+1}'])
        with col2_tab1:
            st.number_input(':red[Capacity]',min_value=1,key=f'company_capacity{i+1}',label_visibility=visibility)
        with col3_tab1:
            st.multiselect(':red[Clients]',
                           st.session_state['clients_names'],
                           key=f'clients_selected{i+1}',
                           label_visibility=visibility)
        charika=company(st.session_state[f'company_name{i+1}'],
                        st.session_state[f'company_capacity{i+1}'],
                        st.session_state[f'clients_selected{i+1}'])
        if charika.name not in [i.name for i in companies] and len(charika.client):
            companies.append(charika)
            choices.update({charika.name:[]})
    with col1_but:
        if st.button('ADD',key='add_company',help='Add a new company'):
            st.session_state.n_company += 1
            st.experimental_rerun()
    with col2_but:
        if st.session_state.n_company >1:
            if st.button('REMOVE',key='remove_company',help='Remove company'):
                st.session_state.n_company -= 1
                if len(st.session_state['company_names'])>st.session_state.n_company:
                    st.session_state['company_names'].pop()
                st.experimental_rerun()

with Tab2:
    col1_tab2,col2_tab2=st.columns([1,2])
    col1_but,col2_but=st.columns([0.5,8])
    for i in range(st.session_state.n_client):
        visibility='collapsed'
        if i==0:
            visibility='visible'
        with col1_tab2:
            if (st.text_input(':red[Name]',key=f'client_name{i+1}',label_visibility=visibility) 
                and st.session_state[f'client_name{i+1}'] 
                not in st.session_state['clients_names']):
                if len(st.session_state['clients_names'])>i:
                    st.session_state['clients_names'][i]=st.session_state[f'client_name{i+1}']
                else:
                    st.session_state['clients_names'].append(st.session_state[f'client_name{i+1}'])
                st.experimental_rerun()
        with col2_tab2:
            st.multiselect(':red[Companies]',st.session_state['company_names'],key=f'company_selected{i+1}',label_visibility=visibility)
        client_name=client(st.session_state[f'client_name{i+1}'],
                           st.session_state[f'company_selected{i+1}'])
        if client_name.name not in [i.name for i in clients] and len(client_name.company) :
            clients.append(client_name)
    with col1_but:
        if st.button('ADD',key='add_client',help='Add a new client'):
            st.session_state.n_client += 1
            st.experimental_rerun()
    with col2_but:
        if st.session_state.n_client >1:
            if st.button('REMOVE',key='remove_client',help='Remove client'):
                st.session_state.n_client -= 1
                if len(st.session_state['clients_names'])>st.session_state.n_client:
                    st.session_state['clients_names'].pop()
                st.experimental_rerun()

def test():
    for i in range(st.session_state.n_company):
        if not st.session_state[f'clients_selected{i+1}']:
            return False
    for i in range(st.session_state.n_client):
        if not st.session_state[f'company_selected{i+1}']:
            return False
    return True

if button:
    if test():
        st.markdown(
        """
        <style>
            .stProgress {
                display: block;
            }
        </style>""",
        unsafe_allow_html=True,
        )
        i=0
        while i<len(clients):
            breaking=False
            for z in choices.values():
                if clients[i].name in z:
                    breaking=True
                    break
            if not breaking:
                for j in clients[i].company:
                    index=-1
                    for k in companies:
                        if k.name==j:
                            index=companies.index(k)
                            break
                    if index!=-1:
                        if clients[i].name in companies[index].client:
                            if len(choices[j])<companies[index].capacity:
                                choices[j].append(clients[i].name)
                                break
                            else:
                                max_pos,max_index = max_position(choices[j],index,companies)
                                if max_pos>companies[index].client.index(clients[i].name):
                                    bnadem = choices[j][max_index]
                                    choices[j][max_index]=clients[i].name
                                    for k in clients:
                                        if k.name==bnadem:
                                            i=clients.index(k)-1
                                            break
                                    break
            i=i+1
        for i in st.session_state['clients_names']:
            st.session_state['graph'].node(i)
        for i in choices.keys():
            st.session_state['graph'].node(i,shape='box')
            for j in choices[i]:
                st.session_state['graph'].edge(i,j)
        for i in range(1,len(choices)+1):
            time.sleep(0.5)
            text=f'Operation in progress...{i*(int(100/len(choices)))}%'
            if i==len(choices):
                text='Terminer'
            my_bar.progress(i*(int(100/len(choices))),text=text)
        st.download_button(label="Download", data=st.session_state['graph'].pipe(format='png'), file_name="graph.png", mime='image/png',help='Download the graph')
        st.graphviz_chart(st.session_state['graph'])
    else:
        st.error('Please fill all the fields')
