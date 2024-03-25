import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scoress):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title("Training...")
    plt.xlabel('Number of games')
    plt.ylabel('scores')
    plt.plot(scores)
    plt.plot(mean_scoress)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scoress)-1, mean_scoress[-1], str(mean_scoress[-1]))