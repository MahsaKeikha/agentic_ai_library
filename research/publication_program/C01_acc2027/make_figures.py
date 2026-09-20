from pathlib import Path
import csv
import math
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

ROOT=Path(__file__).resolve().parent
FIG=ROOT/'figures'
FIG.mkdir(exist_ok=True)

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.size': 8.5,
    'axes.titlesize': 9.5,
    'axes.labelsize': 8.5,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7.3,
    'figure.dpi': 180,
    'savefig.dpi': 300,
})

fig, ax = plt.subplots(figsize=(7.2, 3.1))
ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis('off')

def box(x,y,w,h,text,lw=1.1):
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.04,rounding_size=0.10',fill=False,linewidth=lw)
    ax.add_patch(p)
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=8.2)
    return p

def arrow(x1,y1,x2,y2,style='-|>',lw=1.0,ls='-'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=9,linewidth=lw,linestyle=ls))

box(0.3,2.2,2.1,1.35,'Agent team\nproposes tool action')
box(3.0,2.05,2.45,1.65,'AESC supervisor\nwinning set +\ntransition filter',lw=1.4)
box(6.2,2.2,2.15,1.35,'Tool gateway\nexecutes enabled\naction')
box(9.1,2.2,2.5,1.35,'Environment /\nworkflow state')
arrow(2.4,2.88,3.0,2.88)
arrow(5.45,2.88,6.2,2.88)
arrow(8.35,2.88,9.1,2.88)
arrow(10.35,2.2,10.35,1.35)
arrow(10.35,1.35,4.3,1.35)
arrow(4.3,1.35,4.3,2.05)
ax.text(7.3,1.05,'state and event feedback',ha='center',va='center',fontsize=7.5)
box(2.85,4.55,2.0,0.9,'Authority state\nvalid / revoked')
box(5.05,4.55,2.0,0.9,'Evidence state\nfresh / stale')
box(7.25,4.55,2.0,0.9,'Human review\navailable / marked')
arrow(3.85,4.55,3.85,3.72)
arrow(6.05,4.55,5.0,3.70)
arrow(8.25,4.55,5.25,3.55)
ax.text(3.05,0.35,'Controllable: agent and tool choices',fontsize=7.4)
ax.text(7.0,0.35,'Uncontrollable: revocation, expiry, faults',fontsize=7.4)
fig.tight_layout(pad=0.4)
fig.savefig(FIG/'fig1_architecture.pdf',bbox_inches='tight')
fig.savefig(FIG/'fig1_architecture.png',bbox_inches='tight')
plt.close(fig)

fig, ax = plt.subplots(figsize=(7.2, 3.2))
ax.set_xlim(-0.5,10.5); ax.set_ylim(-0.5,5.4); ax.axis('off')
pos={0:(0.5,2.6),1:(2.2,2.6),2:(4.4,4.0),3:(4.4,1.2),4:(6.5,1.2),5:(8.8,4.0),6:(4.5,2.6),7:(8.8,1.2)}
labels={0:'start',1:'assessed',2:'binding\nsecured',3:'unsecured\ncommitment',4:'binding\ninvalidated',5:'complete',6:'human\nreview',7:'protected\nviolation'}

for s,(x,y) in pos.items():
    c=Circle((x,y),0.48,fill=False,linewidth=1.2)
    ax.add_patch(c)
    ax.text(x,y,labels[s],ha='center',va='center',fontsize=7.2)
    if s in (5,6):
        ax.add_patch(Circle((x,y),0.40,fill=False,linewidth=0.8))
    if s==7:
        ax.text(x,y-0.75,'forbidden',ha='center',fontsize=7.0)

def edge(a,b,label,curve=0.0,lw=1.0,ls='-'):
    x1,y1=pos[a]; x2,y2=pos[b]
    arr=FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=8,
                        connectionstyle=f'arc3,rad={curve}',linewidth=lw,linestyle=ls,
                        shrinkA=34,shrinkB=34)
    ax.add_patch(arr)
    mx=(x1+x2)/2; my=(y1+y2)/2 + (0.35 if curve>0 else -0.35 if curve<0 else 0.20)
    ax.text(mx,my,label,ha='center',va='center',fontsize=6.7)

edge(0,1,'assess')
edge(1,2,'bind authority / evidence',curve=0.05)
edge(1,3,'locally legal precursor',curve=-0.05,lw=1.6)
edge(1,6,'request review',curve=0.0)
edge(2,5,'protected action')
edge(3,5,'protected action',curve=0.12)
edge(3,4,'uncontrollable invalidation',ls='--',lw=1.4)
edge(4,7,'protected action')
ax.text(4.3,0.15,'AESC suppresses the first controllable edge into the losing region.',ha='center',fontsize=7.5)
ax.annotate('suppressed by AESC',xy=(3.5,1.65),xytext=(1.65,0.75),fontsize=7.0,
            arrowprops=dict(arrowstyle='->',linewidth=0.9))
fig.tight_layout(pad=0.3)
fig.savefig(FIG/'fig2_task_automaton.pdf',bbox_inches='tight')
fig.savefig(FIG/'fig2_task_automaton.png',bbox_inches='tight')
plt.close(fig)

with open(ROOT/'results'/'case_study_summary.csv',newline='') as f:
    case=list(csv.DictReader(f))
with open(ROOT/'results'/'scaling_summary.csv',newline='') as f:
    scaling=list(csv.DictReader(f))
with open(ROOT/'results'/'vulnerability_survey.csv',newline='') as f:
    survey=list(csv.DictReader(f))

cases=['software_release','industrial_digital_twin','agewell_support','smart_city']
case_labels=['Software\nrelease','Digital\ntwin','AgeWell\nsupport','Smart\ncity']
lookup={(r['case'],r['controller']):r for r in case}
x=list(range(len(cases)))
width=0.24
fig,ax=plt.subplots(figsize=(7.2,3.0))
vals_un=[100*float(lookup[(c,'unconstrained')]['violation']) for c in cases]
vals_pw=[100*float(lookup[(c,'pointwise_gate')]['deadlock']) for c in cases]
vals_a=[100*(float(lookup[(c,'aesc')]['violation'])+float(lookup[(c,'aesc')]['deadlock'])) for c in cases]
ax.bar([i-width for i in x],vals_un,width,label='Unconstrained: violation')
ax.bar(x,vals_pw,width,label='Pointwise gate: deadlock')
ax.bar([i+width for i in x],vals_a,width,label='AESC: violation + deadlock')
ax.set_ylabel('Adverse outcome rate (%)')
ax.set_xticks(x,case_labels)
ax.set_ylim(0,max(vals_un+vals_pw)*1.28)
ax.grid(axis='y',alpha=0.25,linewidth=0.6)
ax.legend(frameon=False,ncol=3,loc='upper center',bbox_to_anchor=(0.5,1.14))
for i,v in enumerate(vals_un): ax.text(i-width,v+0.25,f'{v:.1f}',ha='center',fontsize=7)
for i,v in enumerate(vals_pw): ax.text(i,v+0.25,f'{v:.1f}',ha='center',fontsize=7)
for i,v in enumerate(vals_a): ax.text(i+width,0.28,'0',ha='center',fontsize=7)
fig.tight_layout(pad=0.5)
fig.savefig(FIG/'fig3_outcomes.pdf',bbox_inches='tight')
fig.savefig(FIG/'fig3_outcomes.png',bbox_inches='tight')
plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(7.2,3.0))
ax=axes[0]
states=[int(r['states']) for r in scaling]
times=[float(r['median_synthesis_ms']) for r in scaling]
ax.plot(states,times,marker='o',linewidth=1.4)
ax.set_xscale('log'); ax.set_yscale('log')
ax.set_xlabel('Plant states')
ax.set_ylabel('Median synthesis time (ms)')
ax.grid(True,which='both',alpha=0.25,linewidth=0.6)
ax.set_title('Finite-state synthesis scaling')
ax.text(0.04,0.92,'22.3 ms at 2,000 states',transform=ax.transAxes,fontsize=7.1,va='top')

ax=axes[1]
ss=[int(r['states']) for r in survey]
prev=[100*float(r['vulnerability_prevalence']) for r in survey]
ax.plot(ss,prev,marker='s',linewidth=1.4)
ax.set_xscale('log')
ax.set_ylim(0,105)
ax.set_xlabel('Random stress-plant states')
ax.set_ylabel('Plants with precursor vulnerability (%)')
ax.grid(True,which='both',alpha=0.25,linewidth=0.6)
ax.set_title('Pointwise-gate insufficiency stress test')
ax.text(0.04,0.08,'Dense random plants; not a real-world prevalence estimate',transform=ax.transAxes,fontsize=6.7)
fig.tight_layout(pad=0.6,w_pad=1.2)
fig.savefig(FIG/'fig4_scaling_vulnerability.pdf',bbox_inches='tight')
fig.savefig(FIG/'fig4_scaling_vulnerability.png',bbox_inches='tight')
plt.close(fig)
