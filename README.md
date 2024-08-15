# 5 antena Problem 

In this code (program) I solve the 5 antenna problem In which you have to place 5 antennas (a,b,c,d,e) on a 6x6 grid in such a way that maximum area is covered by their  signals.Each antenna covers 5 blocks on a grid. One its own, and four neighbours, up, down, left and right. So fitness value is the total area covered by all 5 antennas. You are provided with initial 3 chromosomes
Selection:  
When the fitness value of all three chromosomes is calculated, we select the worst 2 chromosomes for cross over while the best chromosome passes to next generation as it is. 
Mutation: 
ONLY the worst chromosome is mutated out of the three. For mutation ALL the antennas, move upwards, i.e. their y value is decremented by 1.
