import matplotlib.pyplot as plt # type: ignore

def create_histogram(data):
    
    # Extract individual components
    frequency_labels = [entry[0] for entry in data]
    normal_percentages = [entry[1] for entry in data]
    c_section_percentages = [entry[2] for entry in data]

    # Bar settings
    bar_width = 0.35
    indices = range(len(frequency_labels))
    offset = [i + bar_width for i in indices]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(indices, normal_percentages, width=bar_width, label="Normal Delivery %", color='skyblue')
    plt.bar(offset, c_section_percentages, width=bar_width, label="C-Section Delivery %", color='salmon')
    plt.xlabel("Birth Frequency")
    plt.ylabel("Delivery Percentage")
    plt.title("Delivery Methods by Birth Frequency")
    plt.legend()
    plt.show()
