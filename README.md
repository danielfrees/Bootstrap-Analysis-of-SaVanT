# Bootstrap-Analysis-of-SaVanT
![title pic](https://github.com/danielfrees/Bootstrap-Analysis-of-SaVanT/blob/73143d11660c096e5ff3725151e62345cd586f34/images/Screen%20Shot%202021-11-13%20at%201.24.25%20PM.png)

Three components:
1. Data pipeline for converting sample-signature matrix data to pandas dataframes
2. Scripts that investigate the actual data and then run Monte Carlo simulations on sample-signature matrix data (currently with the purpose of investigating preliminary results from SaVanT, a web-based molecular signature software).
3. Exploratory analysis in R with sample-signature matrix data

Note: Daniel's analysis "Bootstrap_Analysis_B_Cells_Pneumonia.ipynb" has a secondary purpose of serving as a guide to our team's workflow & the bootstrapping process, and therefore has a lot of markdown code and explanation. If you're hoping to better understand the workflow of this project, that is a great place to start.

Below is our final report!<br/>



## SaVanT: Differentiating Pneumonia and Skin Disease Pathologies using Molecular Signatures

*Group:* CASB_58_Other, *Mascot:* Bony-Eared Assfish, *Team Members:* Daniel Frees, Neha Bhongir, Brian Chang, Melton Zheng, Theresa Papikian, Suraj Doshi 

## Abstract: 

This paper seeks to determine the utility of sample-wise molecular signature data for differentiating closely related disease pathologies from one another. SaVanT, a molecular-signature visualization and analysis software produced in 2017 under Professor Matteo Pellegrini, establishes a novel method of molecular signature analysis allowing individual samples to be compared with one another (sample-signature matrix data)1. In this research extension, Python-based analyses were performed on this sample-signature matrix data to investigate four hypotheses involving pneumonia pathologies and skin diseases. Due to the sample-by-sample nature of the molecular signature output data from SaVanT, each of these analyses was able to employ the use of modern bootstrapping techniques. Probabilistic p-value computation based on null hypothesis simulations yielded 63.6% significant results across all analyses performed. In particular, it was found that influenza pneumonia and bacterial pneumonia patients can be differentiated based on their relative HPCA B Cell and HBA CD19+ B Cell signature scores, as well as their relative neutrophil signature scores. It was also found that leprosy lesion samples have significantly elevated macrophage signature scores compared to non-leprosy lesion samples. Given the high yield of significant results, it is concluded that sample-wise molecular signature data is a valuable resource which warrants further research.

## Introduction:<br/>

Molecular signatures are collections of genetic markers that can be used to identify particular cell, tissue, or disease phenotypes2. In the last couple decades, several large databases of molecular signatures have been established, along with integrated software for analyzing gene expression data and its correlation with these molecular signatures. However, until the creation of SaVanT, there existed no molecular signature visualization tools that preserved the integrity of individual samples in the signature score output1. Matteo Pellegrini and the other creators of SaVant aimed to fill this gap with the creation of their novel web-based tool SaVanT which enables detailed analysis of gene expression datasets by creating signature correlations on a sample-by-sample basis. SaVanT remains one of the only tools that allows users to see how individual samples compare with one another while conducting analysis on large expression profiles.<br/>

In addition to creating SaVanT, Pellegrini and his team performed preliminary analysis on several datasets using the tool. The two relevant datasets to this extension of research are a pneumonia patient gene expression dataset and a skin disease lesion sample dataset. From their analysis, Pellegrini et. al. made a number of qualitative claims that, if true, could be used to distinguish between related disease pathologies1. This paper aims to investigate four such claims quantitatively and test for their significance. For details on these four claims, refer to the Methods section.<br/>

The goal of the following analysis for all four claims was to determine if sample-wise signature correlation data can be used to significantly differentiate similar disease pathologies. If so, sample-wise signature correlation data should be considered an extremely valuable resource for researchers hoping to better understand the underlying differences between related diseases. Furthermore, if sample-wise signature correlation data can identify highly statistically significant differences between groups, it could have clinical utility for increasing diagnosis accuracy and prescription efficacy.

## Methods:<br/>
First, the SaVanT software was used to generate sample-signature matrix output for the same pneumonia and skin disease datasets investigated by Matteo Pellegrini and his team. Z-score normalization was applied to all signature scores. Next, a data pipeline was designed to convert sample-signature matrices into pandas dataframes. Basic text parsing was utilized to properly fill the data frame with corresponding signature score values from each cell of the sample-signature matrix. After the data pipeline was finished, the following hypotheses were formed based on qualitative claims made by Matteo Pellegrini and his team in their original paper on SaVanT:

Claim 1: Influenza pneumonia patients have enriched signature score values for B cells compared to the signature scores of bacterial pneumonia patients.<br/>
Claim 2: Bacterial pneumonia patients have elevated signature scores for neutrophils relative to the signature scores of influenza pneumonia patients.<br/>
Claim 3: Leprosy lesion samples have elevated signature scores for macrophages compared to the signature scores of non-leprosy lesion samples.<br/>
Claim 4: Patients with Stevens Johnsons disease have elevated hematopoietic cell signatures compared to normal patients and patients with other skin diseases.<br/>

The following experimental statistic was used to quantify the results for each of the above claims:

Let Z<sub>A</sub> = Average combined signature z-score for relevant signatures in Group A<br/>
Let Z<sub>B</sub> = Average combined signature z-score for relevant signatures in Group B<br/>
Difference between groups = Z<sub>A</sub> - Z<sub>B</sub><br/>

To determine significance of the experimental result for each claim, null hypothesis Monte Carlo simulations were generated via bootstrapping of the original data. The null hypothesis was that differences between groups were due to random chance. Thus, null hypothesis simulation generation involved pooling data from each experimental group into a single ‘population’ data pool, followed by resampling with replacement from this ‘population’ data into simulation groups of the same sample size as the original experiment. Ten thousand null hypothesis simulations were run. Null hypothesis distributions were then visualized, and finally two-tailed probabilistic p-values were calculated for each claim.<br/>

In addition to quantification and significance testing of the four claims in Python, exploratory analysis was performed in R. The goal of this analysis was to determine compatibility between sample-signature matrix data and popular R packages, given that R is another highly popular language for computational biologists. Visualization and standard statistical t-test methods were performed in R with perfect compatibility.<br/>

## Results:<br/>
(Note: We used an alpha threshold of p < 0.05 to indicate significance. Significant p-values are bolded)

*Claim 1: Influenza pneumonia is categorized by higher signature scores for B cells.*

Main analysis (Combined B Cells): Experimental Diff (Influenza – Bacterial) = 0.033898, p = 0.7638<br/>
Sub-analysis (WRS B Cells): Experimental Diff (Influenza – Bacterial) = 0.0266023, p = 0.0675<br/>
Sub-analysis (HPCA B Cells): Experimental Diff (Influenza – Bacterial) = 0.177628, **p = 0.0041**<br/>
Sub-analysis (HBA CD19+ B Cells): Experimental Diff (Influenza – Bacterial) = -0.23832, **p = 0.0071**<br/>

*Claim 2: Bacterial pneumonia is categorized by higher signature scores for neutrophils.*

Main analysis (Combined Neutrophils): Experimental Diff (Bacterial – Influenza)= 0.642597,  **p = 0.0000**<br/>
Sub-analysis (WRS Neutrophils): Experimental Diff (Bacterial – Influenza)= 0.438424,  **p = 0.0027**<br/>
Sub-analysis (HPCA-LPS Neutrophils): Experimental Diff (Bacterial – Influenza)= 0.505675, **p = 0.0002**<br/>
Sub-analysis (HPCA Neutrophils): Experimental Diff (Bacterial – Influenza)= 0.983693, **p = 0.0001**<br/>

*Claim 3: Leprosy lesions are categorized by higher signature scores for macrophages.*

Main analysis (Combined Macrophages): Experimental Diff (Leprosy – Others)= 0.0041, **p = 0.0000**<br/>

*Claim 4: Stevens Johnsons disease is categorized by higher signature scores for hematopoietic cells.*

Analysis #1(WRS Hematopoietic Cells):Experimental Diff (SJ – Other)= 48.430840*, p = 0.2928<br/>
Analysis #2(DermDB Hematopoietic Cells): Experimental Diff (SJ – Other)= 148.682527*, p = 0.2143<br/>
*Claim 4 Only: Note that Raw signature scores used for experimental differences instead of z-scores


*Overall Signal:* <br/>
100% * ( significant findings / total comparisons performed ) = 63.6% overall signal

## Discussion:<br/>

Recall that the overall goal of this paper is to determine the utility of sample-wise molecular signature data, based on its potential for identifying statistically significant differences between various disease pathologies. Overall, the incredibly high signal of 63.6% significant findings across eleven comparisons suggests that analysis of sample-signature matrix data has great potential for identifying differences between related diseases. Of these significant findings, all of them fell below even an incredibly strict alpha value of p = 0.01 (prior to multiple comparisons correction). The high signal combined with extremely low p-values suggests that analysis on sample-wise molecular signature data has great potential for noteworthy findings in the realm of disease classification.<br/>

Furthermore, this paper identified several intriguing differences between influenza pneumonia patients and bacterial pneumonia patients. For claim 1, the influenza pneumonia group demonstrated significantly elevated HPCA B Cell scores, while the bacterial pneumonia group had significantly elevated HBA CD19+ B cell scores. Claim 2 found significantly higher neutrophil signature scores in bacterial pneumonia patients compared to influenza pneumonia patients. Further biochemical analysis of these results could potentially elucidate differences in the mechanisms of immune cell response to viral versus bacterial pathogens. Furthermore, if these findings are confirmed by future analysis on additional datasets, they would suggest that specific pneumonia pathology could potentially be better diagnosed by including analysis of the patient’s molecular signature fingerprint in clinical assessments. Importantly, incorporation of sample molecular signature correlation data into diagnostics might help to prevent unnecessary antibiotic prescriptions.<br/>
	
To continue, claim 3 found that leprosy lesions were characterized by elevated macrophage signature scores compared to both other skin diseases and normal skin. This finding implies that leprosy lesions require greater attention from macrophages, either because of their role in immune response or their role in maintaining homeostasis of the skin3.<br/>
	
In summary, the high significance signal across all comparisons and exciting preliminary findings in pneumonia and skin disease suggest that sample-wise molecular signature analysis is highly valuable. Confirmation of the preliminary findings in pneumonia and skin disease would be a massive contribution to each respective field, and new research into differences among other disease families might yield exciting discoveries.
	
## Appendix:

## References:

Lopez, David, et al. “SaVanT: a Web-Based Tool for the Sample-Level Visualization of Molecular Signatures in Gene Expression Profiles.” BMC Genomics, BioMed Central, 25 Oct. 2017, bmcgenomics.biomedcentral.com/articles/10.1186/s12864-017-4167-7. 

Sung, Jaeyun, et al. “Molecular Signatures from Omics Data: From Chaos to Consensus.” Biotechnology Journal, U.S. National Library of Medicine, 23 Apr. 2012, www.ncbi.nlm.nih.gov/pmc/articles/PMC3418428/. 

Yanez, Diana A, et al. “The Role of Macrophages in Skin Homeostasis.” Pflugers Archiv: European Journal of Physiology, U.S. National Library of Medicine, Apr. 2017, www.ncbi.nlm.nih.gov/pmc/articles/PMC5663320/. 

Source Code: https://github.com/danielfrees/Bootstrap-Analysis-of-SaVanT


## Null Hypothesis Distribution Figures:

 Claim 1:

![dist1](https://github.com/danielfrees/Bootstrap-Analysis-of-SaVanT/blob/8707dcd96c88829f74ae12cb02590d24f8a3a411/images/claim1_1.png)
![dist2](https://github.com/danielfrees/Bootstrap-Analysis-of-SaVanT/blob/8707dcd96c88829f74ae12cb02590d24f8a3a411/images/claim1_2.png)


Claim 2:

![dist3](https://github.com/danielfrees/Bootstrap-Analysis-of-SaVanT/blob/8707dcd96c88829f74ae12cb02590d24f8a3a411/images/claim2_1.png)
![dist4](https://github.com/danielfrees/Bootstrap-Analysis-of-SaVanT/blob/8707dcd96c88829f74ae12cb02590d24f8a3a411/images/claim2_2.png)

Claim 3:

![Combined Macrophage Signature Score (Leprosy - Other)](https://github.com/danielfrees/Bootstrap-Analysis-of-SaVanT/blob/8707dcd96c88829f74ae12cb02590d24f8a3a411/images/claim3.png)


Claim 4:

![dist5](https://github.com/danielfrees/Bootstrap-Analysis-of-SaVanT/blob/8707dcd96c88829f74ae12cb02590d24f8a3a411/images/claim4.png)

