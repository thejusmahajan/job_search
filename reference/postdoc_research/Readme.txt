I developed an Individual based model for Nodularia in the 
baltic sea based on Beckmann et al. (2019).
Simulated the topt evolution.
Reached good aggreement with the published experimental values in Medwed et al. (2024).
Found that SST ERA5 data was underrepresenting the cooling phase of 1987.
This led me to view the seemingly trustworthy satellite data with suspicion.
The reason was that the day temp measured by the satelliete is just the temp of the 
surface sea which is warmer than the inner flesh where most events happen.
Modelled a gaussian cold pulse in by studying the reported Baltic sea temperatures.
Incorporated Beckmann's trait diffusion model to successfully model the Nodularia.
Worked with experimentalists doing resurruction experiments.
Got acquainted with the experimental methods, NGS, Blast etc. during the post doc phase which
led me to the amazing world of Bioinformatics and Biostatistics.
Worked with climate data, ocean data.
Worked with GOTM-FABM 1d model to include trait diffusion in cyanobacterial life cycle model
in a 1d water column simulating Baltic sea conditions. Note that this is different from the IBM model.
This is a compartment based concentration model or an Eulerian model while IBM was a lagrangian model.
IBM cannot be implemented directly with GOTM-FABM because GOTM works with concentration rather than
particles.
Did hindcast and forecast studies.
Found that along with the topt evolution, the TPC parameters are also important for the survival
 and success of nodularia in Baltic sea.
Replicated experimental topt values with in the error bar. The SGV was underrepresented which is
the limitation of the 0d model but still good results.
Also found that SGV in the akinete population is extremely important in the bloom success.
As an accident, we modelled the starting akinete germination based on stochaticity.
Assumed that the germinates were 0 in winter and came from the stored akinetes based on the 
germination probability.
It so happened that a slight change of an input file caused a shift of predicted topt about 1 degrees.
It was later found that the fortrans way of generating random numbers is the reason. The change in
the memory shift of the two input files caused a different random numbers to be generated and 
it wokes up akinetes having different set of topt. This then cascaded into the future to cause the 
1 degree shift. So we solved the problem by assuming a SGV in the germinates as well as akinetes and
a large akinete SGV population.

Although I didn't published yet, there is significant results and the project is in a very good trajectory.
I worked on even after my contract was completed.
I found that a small working model is necessary to build a big complex model.
My major drawback in the early phase was that I had to start from the scratch.
A small working IBM model, in an idealized situation, then building it step by step by adding 
features led me to this good results.

