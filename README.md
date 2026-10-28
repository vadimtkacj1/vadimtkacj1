<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img alt="Vadim Tkachenko — AI Engineer" src="assets/header-light.svg" width="100%">
</picture>

I build AI products end to end — from data and model training to the API and the interface people actually use. I work with LLMs and train my own vision and ranking models, and my full-stack background means they ship as working products, not notebooks.

**Currently:** going deeper into retrieval (RAG) and evaluating LLM output.  
**Open to** AI engineering roles and freelance projects · [LinkedIn](https://www.linkedin.com/in/vadim-tkachenko-19842b241) · [vadim.tkach1378@gmail.com](mailto:vadim.tkach1378@gmail.com)

### Selected work

| Project | Result | Stack |
|---|---|---|
| [**hybrid-recommender**](https://github.com/vadimtkacj1/hybrid-recommendation-system-diplom) · thesis | Matches people by YouTube history: TF-IDF, sentence embeddings and ALS blended, MMR re-ranking, cold start. Full product with OAuth, Takeout import and live chat | FastAPI · sentence-transformers · implicit · React |
| [**vessel-segmentation**](https://github.com/vadimtkacj1/vessel-segmentation) | Retinal vessels on fundus images with DeepLabV3+ / ResNet-101, pixel IoU 0.944 over both classes | PyTorch · segmentation-models · Albumentations |
| [**brain-tumour-segmentation**](https://github.com/vadimtkacj1/brain-tumour-segmentation) | Three tumour sub-regions from 4-sequence MRI. Three architectures compared; Attention U-Net reaches about half the baseline's validation loss | PyTorch · h5py |
| [**lora-fine-tuning-service**](https://github.com/vadimtkacj1/fine-tuning-llama) | REST service that fine-tunes Llama 3 8B with 4-bit QLoRA on uploaded dialogues | FastAPI · Transformers · PEFT · bitsandbytes |
| [**real-estate-appraisal**](https://github.com/vadimtkacj1/real-estate-appraisal-agent) | An LLM parses a free-text listing, XGBoost prices it, the LLM explains the estimate | Gemini · XGBoost · Gradio |
| [**clip-retrieval**](https://github.com/vadimtkacj1/clip-retrieval-ai) | Text-to-image and image-to-image search, CLIP vs ResNet-18, cosine vs Euclidean | CLIP · PyTorch · NumPy |

**Product engineering:** [CRM with a Meta Ads analytics panel](https://github.com/vadimtkacj1/aiterra-crm), running in production · FastAPI · React · Docker

<details>
<summary><b>How the recommender ranks people</b></summary>
<br>

```mermaid
flowchart LR
    A[YouTube sync<br/>or Takeout upload] --> B[Watch history]
    B --> C[TF-IDF profile]
    B --> D[Semantic profile<br/>sentence-transformers]
    B --> E[User × Channel matrix] --> F[ALS factors]
    B --> H[Shared videos]
    C & D & F & H --> G[Hybrid score<br/>adaptive weights]
    G --> I[MMR re-ranking] --> J[Matches + explanations]
    B -. under 10 videos .-> K[Cold start:<br/>categories + popularity]
```

</details>

<details>
<summary><b>Vessel segmentation: input, ground truth, prediction, heatmap</b></summary>
<br>

![Fundus image, ground-truth vessels, predicted vessels and heatmap](https://raw.githubusercontent.com/vadimtkacj1/vessel-segmentation/main/assets/prediction.png)

</details>

<details>
<summary><b>Brain tumour segmentation: what the attention gates look at</b></summary>
<br>

![Predicted necrotic core, edema and enhancing tumour](https://raw.githubusercontent.com/vadimtkacj1/brain-tumour-segmentation/main/assets/predicted-regions.png)

![Attention maps from four decoder levels](https://raw.githubusercontent.com/vadimtkacj1/brain-tumour-segmentation/main/assets/attention-maps.png)

</details>

### Training run

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/training-run-dark.svg">
  <img alt="Weekly GitHub contributions over the last 52 weeks drawn as a training curve, with streaks and totals" src="assets/training-run-light.svg" width="100%">
</picture>

### The same year in 3D

Every column is a day, height is the number of contributions. Drag to rotate, scroll to zoom.

<!-- skyline:start -->
```stl
solid contributions
facet normal 0 0 1
outer loop
vertex -1 -1 0
vertex 53.2 -1 0
vertex 53.2 7.2 0
endloop
endfacet
facet normal 0 0 1
outer loop
vertex -1 -1 0
vertex 53.2 7.2 0
vertex -1 7.2 0
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -1 -1 -1.2
vertex 53.2 -1 -1.2
vertex 53.2 -1 0
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex -1 -1 -1.2
vertex 53.2 -1 0
vertex -1 -1 0
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 53.2 7.2 -1.2
vertex -1 7.2 -1.2
vertex -1 7.2 0
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 53.2 7.2 -1.2
vertex -1 7.2 0
vertex 53.2 7.2 0
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -1 7.2 -1.2
vertex -1 -1 -1.2
vertex -1 -1 0
endloop
endfacet
facet normal -1 0 0
outer loop
vertex -1 7.2 -1.2
vertex -1 -1 0
vertex -1 7.2 0
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 53.2 -1 -1.2
vertex 53.2 7.2 -1.2
vertex 53.2 7.2 0
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 53.2 -1 -1.2
vertex 53.2 7.2 0
vertex 53.2 -1 0
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex -1 7.2 -1.2
vertex 53.2 7.2 -1.2
vertex 53.2 -1 -1.2
endloop
endfacet
facet normal 0 0 -1
outer loop
vertex -1 7.2 -1.2
vertex 53.2 -1 -1.2
vertex -1 -1 -1.2
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 0.1 4.1 4.14
vertex 0.9 4.1 4.14
vertex 0.9 4.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 0.1 4.1 4.14
vertex 0.9 4.9 4.14
vertex 0.1 4.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 0.1 4.1 0
vertex 0.9 4.1 0
vertex 0.9 4.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 0.1 4.1 0
vertex 0.9 4.1 4.14
vertex 0.1 4.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 0.9 4.9 0
vertex 0.1 4.9 0
vertex 0.1 4.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 0.9 4.9 0
vertex 0.1 4.9 4.14
vertex 0.9 4.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 0.1 4.9 0
vertex 0.1 4.1 0
vertex 0.1 4.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 0.1 4.9 0
vertex 0.1 4.1 4.14
vertex 0.1 4.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 0.9 4.1 0
vertex 0.9 4.9 0
vertex 0.9 4.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 0.9 4.1 0
vertex 0.9 4.9 4.14
vertex 0.9 4.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 0.1 3.1 3.16
vertex 0.9 3.1 3.16
vertex 0.9 3.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 0.1 3.1 3.16
vertex 0.9 3.9 3.16
vertex 0.1 3.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 0.1 3.1 0
vertex 0.9 3.1 0
vertex 0.9 3.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 0.1 3.1 0
vertex 0.9 3.1 3.16
vertex 0.1 3.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 0.9 3.9 0
vertex 0.1 3.9 0
vertex 0.1 3.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 0.9 3.9 0
vertex 0.1 3.9 3.16
vertex 0.9 3.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 0.1 3.9 0
vertex 0.1 3.1 0
vertex 0.1 3.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 0.1 3.9 0
vertex 0.1 3.1 3.16
vertex 0.1 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 0.9 3.1 0
vertex 0.9 3.9 0
vertex 0.9 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 0.9 3.1 0
vertex 0.9 3.9 3.16
vertex 0.9 3.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 1.1 0.1 4.9
vertex 1.9 0.1 4.9
vertex 1.9 0.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 1.1 0.1 4.9
vertex 1.9 0.9 4.9
vertex 1.1 0.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 1.1 0.1 0
vertex 1.9 0.1 0
vertex 1.9 0.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 1.1 0.1 0
vertex 1.9 0.1 4.9
vertex 1.1 0.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 1.9 0.9 0
vertex 1.1 0.9 0
vertex 1.1 0.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 1.9 0.9 0
vertex 1.1 0.9 4.9
vertex 1.9 0.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 1.1 0.9 0
vertex 1.1 0.1 0
vertex 1.1 0.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 1.1 0.9 0
vertex 1.1 0.1 4.9
vertex 1.1 0.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 1.9 0.1 0
vertex 1.9 0.9 0
vertex 1.9 0.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 1.9 0.1 0
vertex 1.9 0.9 4.9
vertex 1.9 0.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 2.1 6.1 6.09
vertex 2.9 6.1 6.09
vertex 2.9 6.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 2.1 6.1 6.09
vertex 2.9 6.9 6.09
vertex 2.1 6.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 2.1 6.1 0
vertex 2.9 6.1 0
vertex 2.9 6.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 2.1 6.1 0
vertex 2.9 6.1 6.09
vertex 2.1 6.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 2.9 6.9 0
vertex 2.1 6.9 0
vertex 2.1 6.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 2.9 6.9 0
vertex 2.1 6.9 6.09
vertex 2.9 6.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 2.1 6.9 0
vertex 2.1 6.1 0
vertex 2.1 6.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 2.1 6.9 0
vertex 2.1 6.1 6.09
vertex 2.1 6.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 2.9 6.1 0
vertex 2.9 6.9 0
vertex 2.9 6.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 2.9 6.1 0
vertex 2.9 6.9 6.09
vertex 2.9 6.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 9.1 4.1 4.14
vertex 9.9 4.1 4.14
vertex 9.9 4.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 9.1 4.1 4.14
vertex 9.9 4.9 4.14
vertex 9.1 4.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.1 4.1 0
vertex 9.9 4.1 0
vertex 9.9 4.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.1 4.1 0
vertex 9.9 4.1 4.14
vertex 9.1 4.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.9 4.9 0
vertex 9.1 4.9 0
vertex 9.1 4.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.9 4.9 0
vertex 9.1 4.9 4.14
vertex 9.9 4.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 9.1 4.9 0
vertex 9.1 4.1 0
vertex 9.1 4.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 9.1 4.9 0
vertex 9.1 4.1 4.14
vertex 9.1 4.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 9.9 4.1 0
vertex 9.9 4.9 0
vertex 9.9 4.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 9.9 4.1 0
vertex 9.9 4.9 4.14
vertex 9.9 4.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 9.1 3.1 3.16
vertex 9.9 3.1 3.16
vertex 9.9 3.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 9.1 3.1 3.16
vertex 9.9 3.9 3.16
vertex 9.1 3.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.1 3.1 0
vertex 9.9 3.1 0
vertex 9.9 3.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.1 3.1 0
vertex 9.9 3.1 3.16
vertex 9.1 3.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.9 3.9 0
vertex 9.1 3.9 0
vertex 9.1 3.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.9 3.9 0
vertex 9.1 3.9 3.16
vertex 9.9 3.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 9.1 3.9 0
vertex 9.1 3.1 0
vertex 9.1 3.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 9.1 3.9 0
vertex 9.1 3.1 3.16
vertex 9.1 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 9.9 3.1 0
vertex 9.9 3.9 0
vertex 9.9 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 9.9 3.1 0
vertex 9.9 3.9 3.16
vertex 9.9 3.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 9.1 1.1 5.53
vertex 9.9 1.1 5.53
vertex 9.9 1.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 9.1 1.1 5.53
vertex 9.9 1.9 5.53
vertex 9.1 1.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.1 1.1 0
vertex 9.9 1.1 0
vertex 9.9 1.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.1 1.1 0
vertex 9.9 1.1 5.53
vertex 9.1 1.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.9 1.9 0
vertex 9.1 1.9 0
vertex 9.1 1.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.9 1.9 0
vertex 9.1 1.9 5.53
vertex 9.9 1.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 9.1 1.9 0
vertex 9.1 1.1 0
vertex 9.1 1.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 9.1 1.9 0
vertex 9.1 1.1 5.53
vertex 9.1 1.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 9.9 1.1 0
vertex 9.9 1.9 0
vertex 9.9 1.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 9.9 1.1 0
vertex 9.9 1.9 5.53
vertex 9.9 1.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 9.1 0.1 3.16
vertex 9.9 0.1 3.16
vertex 9.9 0.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 9.1 0.1 3.16
vertex 9.9 0.9 3.16
vertex 9.1 0.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.1 0.1 0
vertex 9.9 0.1 0
vertex 9.9 0.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 9.1 0.1 0
vertex 9.9 0.1 3.16
vertex 9.1 0.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.9 0.9 0
vertex 9.1 0.9 0
vertex 9.1 0.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 9.9 0.9 0
vertex 9.1 0.9 3.16
vertex 9.9 0.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 9.1 0.9 0
vertex 9.1 0.1 0
vertex 9.1 0.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 9.1 0.9 0
vertex 9.1 0.1 3.16
vertex 9.1 0.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 9.9 0.1 0
vertex 9.9 0.9 0
vertex 9.9 0.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 9.9 0.1 0
vertex 9.9 0.9 3.16
vertex 9.9 0.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 6.1 9.96
vertex 10.9 6.1 9.96
vertex 10.9 6.9 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 6.1 9.96
vertex 10.9 6.9 9.96
vertex 10.1 6.9 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 6.1 0
vertex 10.9 6.1 0
vertex 10.9 6.1 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 6.1 0
vertex 10.9 6.1 9.96
vertex 10.1 6.1 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 6.9 0
vertex 10.1 6.9 0
vertex 10.1 6.9 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 6.9 0
vertex 10.1 6.9 9.96
vertex 10.9 6.9 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 6.9 0
vertex 10.1 6.1 0
vertex 10.1 6.1 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 6.9 0
vertex 10.1 6.1 9.96
vertex 10.1 6.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 6.1 0
vertex 10.9 6.9 0
vertex 10.9 6.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 6.1 0
vertex 10.9 6.9 9.96
vertex 10.9 6.1 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 5.1 5.53
vertex 10.9 5.1 5.53
vertex 10.9 5.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 5.1 5.53
vertex 10.9 5.9 5.53
vertex 10.1 5.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 5.1 0
vertex 10.9 5.1 0
vertex 10.9 5.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 5.1 0
vertex 10.9 5.1 5.53
vertex 10.1 5.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 5.9 0
vertex 10.1 5.9 0
vertex 10.1 5.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 5.9 0
vertex 10.1 5.9 5.53
vertex 10.9 5.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 5.9 0
vertex 10.1 5.1 0
vertex 10.1 5.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 5.9 0
vertex 10.1 5.1 5.53
vertex 10.1 5.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 5.1 0
vertex 10.9 5.9 0
vertex 10.9 5.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 5.1 0
vertex 10.9 5.9 5.53
vertex 10.9 5.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 4.1 4.9
vertex 10.9 4.1 4.9
vertex 10.9 4.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 4.1 4.9
vertex 10.9 4.9 4.9
vertex 10.1 4.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 4.1 0
vertex 10.9 4.1 0
vertex 10.9 4.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 4.1 0
vertex 10.9 4.1 4.9
vertex 10.1 4.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 4.9 0
vertex 10.1 4.9 0
vertex 10.1 4.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 4.9 0
vertex 10.1 4.9 4.9
vertex 10.9 4.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 4.9 0
vertex 10.1 4.1 0
vertex 10.1 4.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 4.9 0
vertex 10.1 4.1 4.9
vertex 10.1 4.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 4.1 0
vertex 10.9 4.9 0
vertex 10.9 4.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 4.1 0
vertex 10.9 4.9 4.9
vertex 10.9 4.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 2.1 3.16
vertex 10.9 2.1 3.16
vertex 10.9 2.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 2.1 3.16
vertex 10.9 2.9 3.16
vertex 10.1 2.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 2.1 0
vertex 10.9 2.1 0
vertex 10.9 2.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 2.1 0
vertex 10.9 2.1 3.16
vertex 10.1 2.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 2.9 0
vertex 10.1 2.9 0
vertex 10.1 2.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 2.9 0
vertex 10.1 2.9 3.16
vertex 10.9 2.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 2.9 0
vertex 10.1 2.1 0
vertex 10.1 2.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 2.9 0
vertex 10.1 2.1 3.16
vertex 10.1 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 2.1 0
vertex 10.9 2.9 0
vertex 10.9 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 2.1 0
vertex 10.9 2.9 3.16
vertex 10.9 2.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 1.1 4.14
vertex 10.9 1.1 4.14
vertex 10.9 1.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 10.1 1.1 4.14
vertex 10.9 1.9 4.14
vertex 10.1 1.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 1.1 0
vertex 10.9 1.1 0
vertex 10.9 1.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 10.1 1.1 0
vertex 10.9 1.1 4.14
vertex 10.1 1.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 1.9 0
vertex 10.1 1.9 0
vertex 10.1 1.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 10.9 1.9 0
vertex 10.1 1.9 4.14
vertex 10.9 1.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 1.9 0
vertex 10.1 1.1 0
vertex 10.1 1.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 10.1 1.9 0
vertex 10.1 1.1 4.14
vertex 10.1 1.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 1.1 0
vertex 10.9 1.9 0
vertex 10.9 1.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 10.9 1.1 0
vertex 10.9 1.9 4.14
vertex 10.9 1.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 6.1 7.89
vertex 11.9 6.1 7.89
vertex 11.9 6.9 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 6.1 7.89
vertex 11.9 6.9 7.89
vertex 11.1 6.9 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 6.1 0
vertex 11.9 6.1 0
vertex 11.9 6.1 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 6.1 0
vertex 11.9 6.1 7.89
vertex 11.1 6.1 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 6.9 0
vertex 11.1 6.9 0
vertex 11.1 6.9 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 6.9 0
vertex 11.1 6.9 7.89
vertex 11.9 6.9 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 6.9 0
vertex 11.1 6.1 0
vertex 11.1 6.1 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 6.9 0
vertex 11.1 6.1 7.89
vertex 11.1 6.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 6.1 0
vertex 11.9 6.9 0
vertex 11.9 6.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 6.1 0
vertex 11.9 6.9 7.89
vertex 11.9 6.1 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 5.1 12.62
vertex 11.9 5.1 12.62
vertex 11.9 5.9 12.62
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 5.1 12.62
vertex 11.9 5.9 12.62
vertex 11.1 5.9 12.62
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 5.1 0
vertex 11.9 5.1 0
vertex 11.9 5.1 12.62
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 5.1 0
vertex 11.9 5.1 12.62
vertex 11.1 5.1 12.62
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 5.9 0
vertex 11.1 5.9 0
vertex 11.1 5.9 12.62
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 5.9 0
vertex 11.1 5.9 12.62
vertex 11.9 5.9 12.62
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 5.9 0
vertex 11.1 5.1 0
vertex 11.1 5.1 12.62
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 5.9 0
vertex 11.1 5.1 12.62
vertex 11.1 5.9 12.62
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 5.1 0
vertex 11.9 5.9 0
vertex 11.9 5.9 12.62
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 5.1 0
vertex 11.9 5.9 12.62
vertex 11.9 5.1 12.62
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 4.1 7.89
vertex 11.9 4.1 7.89
vertex 11.9 4.9 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 4.1 7.89
vertex 11.9 4.9 7.89
vertex 11.1 4.9 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 4.1 0
vertex 11.9 4.1 0
vertex 11.9 4.1 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 4.1 0
vertex 11.9 4.1 7.89
vertex 11.1 4.1 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 4.9 0
vertex 11.1 4.9 0
vertex 11.1 4.9 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 4.9 0
vertex 11.1 4.9 7.89
vertex 11.9 4.9 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 4.9 0
vertex 11.1 4.1 0
vertex 11.1 4.1 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 4.9 0
vertex 11.1 4.1 7.89
vertex 11.1 4.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 4.1 0
vertex 11.9 4.9 0
vertex 11.9 4.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 4.1 0
vertex 11.9 4.9 7.89
vertex 11.9 4.1 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 3.1 7.49
vertex 11.9 3.1 7.49
vertex 11.9 3.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 3.1 7.49
vertex 11.9 3.9 7.49
vertex 11.1 3.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 3.1 0
vertex 11.9 3.1 0
vertex 11.9 3.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 3.1 0
vertex 11.9 3.1 7.49
vertex 11.1 3.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 3.9 0
vertex 11.1 3.9 0
vertex 11.1 3.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 3.9 0
vertex 11.1 3.9 7.49
vertex 11.9 3.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 3.9 0
vertex 11.1 3.1 0
vertex 11.1 3.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 3.9 0
vertex 11.1 3.1 7.49
vertex 11.1 3.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 3.1 0
vertex 11.9 3.9 0
vertex 11.9 3.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 3.1 0
vertex 11.9 3.9 7.49
vertex 11.9 3.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 2.1 4.9
vertex 11.9 2.1 4.9
vertex 11.9 2.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 2.1 4.9
vertex 11.9 2.9 4.9
vertex 11.1 2.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 2.1 0
vertex 11.9 2.1 0
vertex 11.9 2.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 2.1 0
vertex 11.9 2.1 4.9
vertex 11.1 2.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 2.9 0
vertex 11.1 2.9 0
vertex 11.1 2.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 2.9 0
vertex 11.1 2.9 4.9
vertex 11.9 2.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 2.9 0
vertex 11.1 2.1 0
vertex 11.1 2.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 2.9 0
vertex 11.1 2.1 4.9
vertex 11.1 2.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 2.1 0
vertex 11.9 2.9 0
vertex 11.9 2.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 2.1 0
vertex 11.9 2.9 4.9
vertex 11.9 2.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 1.1 7.89
vertex 11.9 1.1 7.89
vertex 11.9 1.9 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 11.1 1.1 7.89
vertex 11.9 1.9 7.89
vertex 11.1 1.9 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 1.1 0
vertex 11.9 1.1 0
vertex 11.9 1.1 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 11.1 1.1 0
vertex 11.9 1.1 7.89
vertex 11.1 1.1 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 1.9 0
vertex 11.1 1.9 0
vertex 11.1 1.9 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 11.9 1.9 0
vertex 11.1 1.9 7.89
vertex 11.9 1.9 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 1.9 0
vertex 11.1 1.1 0
vertex 11.1 1.1 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 11.1 1.9 0
vertex 11.1 1.1 7.89
vertex 11.1 1.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 1.1 0
vertex 11.9 1.9 0
vertex 11.9 1.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 11.9 1.1 0
vertex 11.9 1.9 7.89
vertex 11.9 1.1 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 12.1 5.1 7.49
vertex 12.9 5.1 7.49
vertex 12.9 5.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 12.1 5.1 7.49
vertex 12.9 5.9 7.49
vertex 12.1 5.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 12.1 5.1 0
vertex 12.9 5.1 0
vertex 12.9 5.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 12.1 5.1 0
vertex 12.9 5.1 7.49
vertex 12.1 5.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 12.9 5.9 0
vertex 12.1 5.9 0
vertex 12.1 5.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 12.9 5.9 0
vertex 12.1 5.9 7.49
vertex 12.9 5.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 12.1 5.9 0
vertex 12.1 5.1 0
vertex 12.1 5.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 12.1 5.9 0
vertex 12.1 5.1 7.49
vertex 12.1 5.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 12.9 5.1 0
vertex 12.9 5.9 0
vertex 12.9 5.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 12.9 5.1 0
vertex 12.9 5.9 7.49
vertex 12.9 5.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 12.1 3.1 14.38
vertex 12.9 3.1 14.38
vertex 12.9 3.9 14.38
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 12.1 3.1 14.38
vertex 12.9 3.9 14.38
vertex 12.1 3.9 14.38
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 12.1 3.1 0
vertex 12.9 3.1 0
vertex 12.9 3.1 14.38
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 12.1 3.1 0
vertex 12.9 3.1 14.38
vertex 12.1 3.1 14.38
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 12.9 3.9 0
vertex 12.1 3.9 0
vertex 12.1 3.9 14.38
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 12.9 3.9 0
vertex 12.1 3.9 14.38
vertex 12.9 3.9 14.38
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 12.1 3.9 0
vertex 12.1 3.1 0
vertex 12.1 3.1 14.38
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 12.1 3.9 0
vertex 12.1 3.1 14.38
vertex 12.1 3.9 14.38
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 12.9 3.1 0
vertex 12.9 3.9 0
vertex 12.9 3.9 14.38
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 12.9 3.1 0
vertex 12.9 3.9 14.38
vertex 12.9 3.1 14.38
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 12.1 2.1 11.64
vertex 12.9 2.1 11.64
vertex 12.9 2.9 11.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 12.1 2.1 11.64
vertex 12.9 2.9 11.64
vertex 12.1 2.9 11.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 12.1 2.1 0
vertex 12.9 2.1 0
vertex 12.9 2.1 11.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 12.1 2.1 0
vertex 12.9 2.1 11.64
vertex 12.1 2.1 11.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 12.9 2.9 0
vertex 12.1 2.9 0
vertex 12.1 2.9 11.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 12.9 2.9 0
vertex 12.1 2.9 11.64
vertex 12.9 2.9 11.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 12.1 2.9 0
vertex 12.1 2.1 0
vertex 12.1 2.1 11.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 12.1 2.9 0
vertex 12.1 2.1 11.64
vertex 12.1 2.9 11.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 12.9 2.1 0
vertex 12.9 2.9 0
vertex 12.9 2.9 11.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 12.9 2.1 0
vertex 12.9 2.9 11.64
vertex 12.9 2.1 11.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 12.1 1.1 12.39
vertex 12.9 1.1 12.39
vertex 12.9 1.9 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 12.1 1.1 12.39
vertex 12.9 1.9 12.39
vertex 12.1 1.9 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 12.1 1.1 0
vertex 12.9 1.1 0
vertex 12.9 1.1 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 12.1 1.1 0
vertex 12.9 1.1 12.39
vertex 12.1 1.1 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 12.9 1.9 0
vertex 12.1 1.9 0
vertex 12.1 1.9 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 12.9 1.9 0
vertex 12.1 1.9 12.39
vertex 12.9 1.9 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 12.1 1.9 0
vertex 12.1 1.1 0
vertex 12.1 1.1 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 12.1 1.9 0
vertex 12.1 1.1 12.39
vertex 12.1 1.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 12.9 1.1 0
vertex 12.9 1.9 0
vertex 12.9 1.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 12.9 1.1 0
vertex 12.9 1.9 12.39
vertex 12.9 1.1 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 6.1 9.96
vertex 13.9 6.1 9.96
vertex 13.9 6.9 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 6.1 9.96
vertex 13.9 6.9 9.96
vertex 13.1 6.9 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 6.1 0
vertex 13.9 6.1 0
vertex 13.9 6.1 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 6.1 0
vertex 13.9 6.1 9.96
vertex 13.1 6.1 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 6.9 0
vertex 13.1 6.9 0
vertex 13.1 6.9 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 6.9 0
vertex 13.1 6.9 9.96
vertex 13.9 6.9 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 6.9 0
vertex 13.1 6.1 0
vertex 13.1 6.1 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 6.9 0
vertex 13.1 6.1 9.96
vertex 13.1 6.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 6.1 0
vertex 13.9 6.9 0
vertex 13.9 6.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 6.1 0
vertex 13.9 6.9 9.96
vertex 13.9 6.1 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 4.1 4.9
vertex 13.9 4.1 4.9
vertex 13.9 4.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 4.1 4.9
vertex 13.9 4.9 4.9
vertex 13.1 4.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 4.1 0
vertex 13.9 4.1 0
vertex 13.9 4.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 4.1 0
vertex 13.9 4.1 4.9
vertex 13.1 4.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 4.9 0
vertex 13.1 4.9 0
vertex 13.1 4.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 4.9 0
vertex 13.1 4.9 4.9
vertex 13.9 4.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 4.9 0
vertex 13.1 4.1 0
vertex 13.1 4.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 4.9 0
vertex 13.1 4.1 4.9
vertex 13.1 4.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 4.1 0
vertex 13.9 4.9 0
vertex 13.9 4.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 4.1 0
vertex 13.9 4.9 4.9
vertex 13.9 4.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 3.1 12.39
vertex 13.9 3.1 12.39
vertex 13.9 3.9 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 3.1 12.39
vertex 13.9 3.9 12.39
vertex 13.1 3.9 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 3.1 0
vertex 13.9 3.1 0
vertex 13.9 3.1 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 3.1 0
vertex 13.9 3.1 12.39
vertex 13.1 3.1 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 3.9 0
vertex 13.1 3.9 0
vertex 13.1 3.9 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 3.9 0
vertex 13.1 3.9 12.39
vertex 13.9 3.9 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 3.9 0
vertex 13.1 3.1 0
vertex 13.1 3.1 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 3.9 0
vertex 13.1 3.1 12.39
vertex 13.1 3.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 3.1 0
vertex 13.9 3.9 0
vertex 13.9 3.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 3.1 0
vertex 13.9 3.9 12.39
vertex 13.9 3.1 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 2.1 7.06
vertex 13.9 2.1 7.06
vertex 13.9 2.9 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 2.1 7.06
vertex 13.9 2.9 7.06
vertex 13.1 2.9 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 2.1 0
vertex 13.9 2.1 0
vertex 13.9 2.1 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 2.1 0
vertex 13.9 2.1 7.06
vertex 13.1 2.1 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 2.9 0
vertex 13.1 2.9 0
vertex 13.1 2.9 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 2.9 0
vertex 13.1 2.9 7.06
vertex 13.9 2.9 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 2.9 0
vertex 13.1 2.1 0
vertex 13.1 2.1 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 2.9 0
vertex 13.1 2.1 7.06
vertex 13.1 2.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 2.1 0
vertex 13.9 2.9 0
vertex 13.9 2.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 2.1 0
vertex 13.9 2.9 7.06
vertex 13.9 2.1 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 1.1 7.06
vertex 13.9 1.1 7.06
vertex 13.9 1.9 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 13.1 1.1 7.06
vertex 13.9 1.9 7.06
vertex 13.1 1.9 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 1.1 0
vertex 13.9 1.1 0
vertex 13.9 1.1 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 13.1 1.1 0
vertex 13.9 1.1 7.06
vertex 13.1 1.1 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 1.9 0
vertex 13.1 1.9 0
vertex 13.1 1.9 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 13.9 1.9 0
vertex 13.1 1.9 7.06
vertex 13.9 1.9 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 1.9 0
vertex 13.1 1.1 0
vertex 13.1 1.1 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 13.1 1.9 0
vertex 13.1 1.1 7.06
vertex 13.1 1.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 1.1 0
vertex 13.9 1.9 0
vertex 13.9 1.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 13.9 1.1 0
vertex 13.9 1.9 7.06
vertex 13.9 1.1 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 6.1 7.89
vertex 14.9 6.1 7.89
vertex 14.9 6.9 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 6.1 7.89
vertex 14.9 6.9 7.89
vertex 14.1 6.9 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 6.1 0
vertex 14.9 6.1 0
vertex 14.9 6.1 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 6.1 0
vertex 14.9 6.1 7.89
vertex 14.1 6.1 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 6.9 0
vertex 14.1 6.9 0
vertex 14.1 6.9 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 6.9 0
vertex 14.1 6.9 7.89
vertex 14.9 6.9 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 6.9 0
vertex 14.1 6.1 0
vertex 14.1 6.1 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 6.9 0
vertex 14.1 6.1 7.89
vertex 14.1 6.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 6.1 0
vertex 14.9 6.9 0
vertex 14.9 6.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 6.1 0
vertex 14.9 6.9 7.89
vertex 14.9 6.1 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 5.1 8.28
vertex 14.9 5.1 8.28
vertex 14.9 5.9 8.28
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 5.1 8.28
vertex 14.9 5.9 8.28
vertex 14.1 5.9 8.28
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 5.1 0
vertex 14.9 5.1 0
vertex 14.9 5.1 8.28
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 5.1 0
vertex 14.9 5.1 8.28
vertex 14.1 5.1 8.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 5.9 0
vertex 14.1 5.9 0
vertex 14.1 5.9 8.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 5.9 0
vertex 14.1 5.9 8.28
vertex 14.9 5.9 8.28
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 5.9 0
vertex 14.1 5.1 0
vertex 14.1 5.1 8.28
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 5.9 0
vertex 14.1 5.1 8.28
vertex 14.1 5.9 8.28
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 5.1 0
vertex 14.9 5.9 0
vertex 14.9 5.9 8.28
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 5.1 0
vertex 14.9 5.9 8.28
vertex 14.9 5.1 8.28
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 4.1 7.49
vertex 14.9 4.1 7.49
vertex 14.9 4.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 4.1 7.49
vertex 14.9 4.9 7.49
vertex 14.1 4.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 4.1 0
vertex 14.9 4.1 0
vertex 14.9 4.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 4.1 0
vertex 14.9 4.1 7.49
vertex 14.1 4.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 4.9 0
vertex 14.1 4.9 0
vertex 14.1 4.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 4.9 0
vertex 14.1 4.9 7.49
vertex 14.9 4.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 4.9 0
vertex 14.1 4.1 0
vertex 14.1 4.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 4.9 0
vertex 14.1 4.1 7.49
vertex 14.1 4.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 4.1 0
vertex 14.9 4.9 0
vertex 14.9 4.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 4.1 0
vertex 14.9 4.9 7.49
vertex 14.9 4.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 2.1 4.9
vertex 14.9 2.1 4.9
vertex 14.9 2.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 2.1 4.9
vertex 14.9 2.9 4.9
vertex 14.1 2.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 2.1 0
vertex 14.9 2.1 0
vertex 14.9 2.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 2.1 0
vertex 14.9 2.1 4.9
vertex 14.1 2.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 2.9 0
vertex 14.1 2.9 0
vertex 14.1 2.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 2.9 0
vertex 14.1 2.9 4.9
vertex 14.9 2.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 2.9 0
vertex 14.1 2.1 0
vertex 14.1 2.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 2.9 0
vertex 14.1 2.1 4.9
vertex 14.1 2.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 2.1 0
vertex 14.9 2.9 0
vertex 14.9 2.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 2.1 0
vertex 14.9 2.9 4.9
vertex 14.9 2.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 1.1 5.53
vertex 14.9 1.1 5.53
vertex 14.9 1.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 1.1 5.53
vertex 14.9 1.9 5.53
vertex 14.1 1.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 1.1 0
vertex 14.9 1.1 0
vertex 14.9 1.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 1.1 0
vertex 14.9 1.1 5.53
vertex 14.1 1.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 1.9 0
vertex 14.1 1.9 0
vertex 14.1 1.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 1.9 0
vertex 14.1 1.9 5.53
vertex 14.9 1.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 1.9 0
vertex 14.1 1.1 0
vertex 14.1 1.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 1.9 0
vertex 14.1 1.1 5.53
vertex 14.1 1.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 1.1 0
vertex 14.9 1.9 0
vertex 14.9 1.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 1.1 0
vertex 14.9 1.9 5.53
vertex 14.9 1.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 0.1 4.9
vertex 14.9 0.1 4.9
vertex 14.9 0.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 14.1 0.1 4.9
vertex 14.9 0.9 4.9
vertex 14.1 0.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 0.1 0
vertex 14.9 0.1 0
vertex 14.9 0.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 14.1 0.1 0
vertex 14.9 0.1 4.9
vertex 14.1 0.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 0.9 0
vertex 14.1 0.9 0
vertex 14.1 0.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 14.9 0.9 0
vertex 14.1 0.9 4.9
vertex 14.9 0.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 0.9 0
vertex 14.1 0.1 0
vertex 14.1 0.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 14.1 0.9 0
vertex 14.1 0.1 4.9
vertex 14.1 0.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 0.1 0
vertex 14.9 0.9 0
vertex 14.9 0.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 14.9 0.1 0
vertex 14.9 0.9 4.9
vertex 14.9 0.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 15.1 6.1 12.14
vertex 15.9 6.1 12.14
vertex 15.9 6.9 12.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 15.1 6.1 12.14
vertex 15.9 6.9 12.14
vertex 15.1 6.9 12.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 15.1 6.1 0
vertex 15.9 6.1 0
vertex 15.9 6.1 12.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 15.1 6.1 0
vertex 15.9 6.1 12.14
vertex 15.1 6.1 12.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 15.9 6.9 0
vertex 15.1 6.9 0
vertex 15.1 6.9 12.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 15.9 6.9 0
vertex 15.1 6.9 12.14
vertex 15.9 6.9 12.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 15.1 6.9 0
vertex 15.1 6.1 0
vertex 15.1 6.1 12.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 15.1 6.9 0
vertex 15.1 6.1 12.14
vertex 15.1 6.9 12.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 15.9 6.1 0
vertex 15.9 6.9 0
vertex 15.9 6.9 12.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 15.9 6.1 0
vertex 15.9 6.9 12.14
vertex 15.9 6.1 12.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 15.1 5.1 8.28
vertex 15.9 5.1 8.28
vertex 15.9 5.9 8.28
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 15.1 5.1 8.28
vertex 15.9 5.9 8.28
vertex 15.1 5.9 8.28
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 15.1 5.1 0
vertex 15.9 5.1 0
vertex 15.9 5.1 8.28
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 15.1 5.1 0
vertex 15.9 5.1 8.28
vertex 15.1 5.1 8.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 15.9 5.9 0
vertex 15.1 5.9 0
vertex 15.1 5.9 8.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 15.9 5.9 0
vertex 15.1 5.9 8.28
vertex 15.9 5.9 8.28
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 15.1 5.9 0
vertex 15.1 5.1 0
vertex 15.1 5.1 8.28
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 15.1 5.9 0
vertex 15.1 5.1 8.28
vertex 15.1 5.9 8.28
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 15.9 5.1 0
vertex 15.9 5.9 0
vertex 15.9 5.9 8.28
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 15.9 5.1 0
vertex 15.9 5.9 8.28
vertex 15.9 5.1 8.28
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 15.1 2.1 3.16
vertex 15.9 2.1 3.16
vertex 15.9 2.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 15.1 2.1 3.16
vertex 15.9 2.9 3.16
vertex 15.1 2.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 15.1 2.1 0
vertex 15.9 2.1 0
vertex 15.9 2.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 15.1 2.1 0
vertex 15.9 2.1 3.16
vertex 15.1 2.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 15.9 2.9 0
vertex 15.1 2.9 0
vertex 15.1 2.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 15.9 2.9 0
vertex 15.1 2.9 3.16
vertex 15.9 2.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 15.1 2.9 0
vertex 15.1 2.1 0
vertex 15.1 2.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 15.1 2.9 0
vertex 15.1 2.1 3.16
vertex 15.1 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 15.9 2.1 0
vertex 15.9 2.9 0
vertex 15.9 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 15.9 2.1 0
vertex 15.9 2.9 3.16
vertex 15.9 2.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 15.1 1.1 11.64
vertex 15.9 1.1 11.64
vertex 15.9 1.9 11.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 15.1 1.1 11.64
vertex 15.9 1.9 11.64
vertex 15.1 1.9 11.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 15.1 1.1 0
vertex 15.9 1.1 0
vertex 15.9 1.1 11.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 15.1 1.1 0
vertex 15.9 1.1 11.64
vertex 15.1 1.1 11.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 15.9 1.9 0
vertex 15.1 1.9 0
vertex 15.1 1.9 11.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 15.9 1.9 0
vertex 15.1 1.9 11.64
vertex 15.9 1.9 11.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 15.1 1.9 0
vertex 15.1 1.1 0
vertex 15.1 1.1 11.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 15.1 1.9 0
vertex 15.1 1.1 11.64
vertex 15.1 1.9 11.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 15.9 1.1 0
vertex 15.9 1.9 0
vertex 15.9 1.9 11.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 15.9 1.1 0
vertex 15.9 1.9 11.64
vertex 15.9 1.1 11.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 6.1 11.11
vertex 16.9 6.1 11.11
vertex 16.9 6.9 11.11
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 6.1 11.11
vertex 16.9 6.9 11.11
vertex 16.1 6.9 11.11
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 6.1 0
vertex 16.9 6.1 0
vertex 16.9 6.1 11.11
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 6.1 0
vertex 16.9 6.1 11.11
vertex 16.1 6.1 11.11
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 6.9 0
vertex 16.1 6.9 0
vertex 16.1 6.9 11.11
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 6.9 0
vertex 16.1 6.9 11.11
vertex 16.9 6.9 11.11
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 6.9 0
vertex 16.1 6.1 0
vertex 16.1 6.1 11.11
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 6.9 0
vertex 16.1 6.1 11.11
vertex 16.1 6.9 11.11
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 6.1 0
vertex 16.9 6.9 0
vertex 16.9 6.9 11.11
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 6.1 0
vertex 16.9 6.9 11.11
vertex 16.9 6.1 11.11
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 5.1 13.75
vertex 16.9 5.1 13.75
vertex 16.9 5.9 13.75
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 5.1 13.75
vertex 16.9 5.9 13.75
vertex 16.1 5.9 13.75
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 5.1 0
vertex 16.9 5.1 0
vertex 16.9 5.1 13.75
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 5.1 0
vertex 16.9 5.1 13.75
vertex 16.1 5.1 13.75
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 5.9 0
vertex 16.1 5.9 0
vertex 16.1 5.9 13.75
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 5.9 0
vertex 16.1 5.9 13.75
vertex 16.9 5.9 13.75
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 5.9 0
vertex 16.1 5.1 0
vertex 16.1 5.1 13.75
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 5.9 0
vertex 16.1 5.1 13.75
vertex 16.1 5.9 13.75
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 5.1 0
vertex 16.9 5.9 0
vertex 16.9 5.9 13.75
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 5.1 0
vertex 16.9 5.9 13.75
vertex 16.9 5.1 13.75
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 4.1 14.79
vertex 16.9 4.1 14.79
vertex 16.9 4.9 14.79
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 4.1 14.79
vertex 16.9 4.9 14.79
vertex 16.1 4.9 14.79
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 4.1 0
vertex 16.9 4.1 0
vertex 16.9 4.1 14.79
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 4.1 0
vertex 16.9 4.1 14.79
vertex 16.1 4.1 14.79
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 4.9 0
vertex 16.1 4.9 0
vertex 16.1 4.9 14.79
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 4.9 0
vertex 16.1 4.9 14.79
vertex 16.9 4.9 14.79
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 4.9 0
vertex 16.1 4.1 0
vertex 16.1 4.1 14.79
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 4.9 0
vertex 16.1 4.1 14.79
vertex 16.1 4.9 14.79
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 4.1 0
vertex 16.9 4.9 0
vertex 16.9 4.9 14.79
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 4.1 0
vertex 16.9 4.9 14.79
vertex 16.9 4.1 14.79
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 3.1 16.84
vertex 16.9 3.1 16.84
vertex 16.9 3.9 16.84
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 3.1 16.84
vertex 16.9 3.9 16.84
vertex 16.1 3.9 16.84
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 3.1 0
vertex 16.9 3.1 0
vertex 16.9 3.1 16.84
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 3.1 0
vertex 16.9 3.1 16.84
vertex 16.1 3.1 16.84
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 3.9 0
vertex 16.1 3.9 0
vertex 16.1 3.9 16.84
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 3.9 0
vertex 16.1 3.9 16.84
vertex 16.9 3.9 16.84
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 3.9 0
vertex 16.1 3.1 0
vertex 16.1 3.1 16.84
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 3.9 0
vertex 16.1 3.1 16.84
vertex 16.1 3.9 16.84
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 3.1 0
vertex 16.9 3.9 0
vertex 16.9 3.9 16.84
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 3.1 0
vertex 16.9 3.9 16.84
vertex 16.9 3.1 16.84
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 2.1 6.09
vertex 16.9 2.1 6.09
vertex 16.9 2.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 2.1 6.09
vertex 16.9 2.9 6.09
vertex 16.1 2.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 2.1 0
vertex 16.9 2.1 0
vertex 16.9 2.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 2.1 0
vertex 16.9 2.1 6.09
vertex 16.1 2.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 2.9 0
vertex 16.1 2.9 0
vertex 16.1 2.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 2.9 0
vertex 16.1 2.9 6.09
vertex 16.9 2.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 2.9 0
vertex 16.1 2.1 0
vertex 16.1 2.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 2.9 0
vertex 16.1 2.1 6.09
vertex 16.1 2.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 2.1 0
vertex 16.9 2.9 0
vertex 16.9 2.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 2.1 0
vertex 16.9 2.9 6.09
vertex 16.9 2.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 1.1 3.16
vertex 16.9 1.1 3.16
vertex 16.9 1.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 16.1 1.1 3.16
vertex 16.9 1.9 3.16
vertex 16.1 1.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 1.1 0
vertex 16.9 1.1 0
vertex 16.9 1.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 16.1 1.1 0
vertex 16.9 1.1 3.16
vertex 16.1 1.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 1.9 0
vertex 16.1 1.9 0
vertex 16.1 1.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 16.9 1.9 0
vertex 16.1 1.9 3.16
vertex 16.9 1.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 1.9 0
vertex 16.1 1.1 0
vertex 16.1 1.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 16.1 1.9 0
vertex 16.1 1.1 3.16
vertex 16.1 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 1.1 0
vertex 16.9 1.9 0
vertex 16.9 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 16.9 1.1 0
vertex 16.9 1.9 3.16
vertex 16.9 1.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 5.1 14.79
vertex 17.9 5.1 14.79
vertex 17.9 5.9 14.79
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 5.1 14.79
vertex 17.9 5.9 14.79
vertex 17.1 5.9 14.79
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 5.1 0
vertex 17.9 5.1 0
vertex 17.9 5.1 14.79
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 5.1 0
vertex 17.9 5.1 14.79
vertex 17.1 5.1 14.79
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 5.9 0
vertex 17.1 5.9 0
vertex 17.1 5.9 14.79
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 5.9 0
vertex 17.1 5.9 14.79
vertex 17.9 5.9 14.79
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 5.9 0
vertex 17.1 5.1 0
vertex 17.1 5.1 14.79
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 5.9 0
vertex 17.1 5.1 14.79
vertex 17.1 5.9 14.79
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 5.1 0
vertex 17.9 5.9 0
vertex 17.9 5.9 14.79
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 5.1 0
vertex 17.9 5.9 14.79
vertex 17.9 5.1 14.79
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 4.1 5.53
vertex 17.9 4.1 5.53
vertex 17.9 4.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 4.1 5.53
vertex 17.9 4.9 5.53
vertex 17.1 4.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 4.1 0
vertex 17.9 4.1 0
vertex 17.9 4.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 4.1 0
vertex 17.9 4.1 5.53
vertex 17.1 4.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 4.9 0
vertex 17.1 4.9 0
vertex 17.1 4.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 4.9 0
vertex 17.1 4.9 5.53
vertex 17.9 4.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 4.9 0
vertex 17.1 4.1 0
vertex 17.1 4.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 4.9 0
vertex 17.1 4.1 5.53
vertex 17.1 4.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 4.1 0
vertex 17.9 4.9 0
vertex 17.9 4.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 4.1 0
vertex 17.9 4.9 5.53
vertex 17.9 4.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 3.1 13.09
vertex 17.9 3.1 13.09
vertex 17.9 3.9 13.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 3.1 13.09
vertex 17.9 3.9 13.09
vertex 17.1 3.9 13.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 3.1 0
vertex 17.9 3.1 0
vertex 17.9 3.1 13.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 3.1 0
vertex 17.9 3.1 13.09
vertex 17.1 3.1 13.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 3.9 0
vertex 17.1 3.9 0
vertex 17.1 3.9 13.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 3.9 0
vertex 17.1 3.9 13.09
vertex 17.9 3.9 13.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 3.9 0
vertex 17.1 3.1 0
vertex 17.1 3.1 13.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 3.9 0
vertex 17.1 3.1 13.09
vertex 17.1 3.9 13.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 3.1 0
vertex 17.9 3.9 0
vertex 17.9 3.9 13.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 3.1 0
vertex 17.9 3.9 13.09
vertex 17.9 3.1 13.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 2.1 9.33
vertex 17.9 2.1 9.33
vertex 17.9 2.9 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 2.1 9.33
vertex 17.9 2.9 9.33
vertex 17.1 2.9 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 2.1 0
vertex 17.9 2.1 0
vertex 17.9 2.1 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 2.1 0
vertex 17.9 2.1 9.33
vertex 17.1 2.1 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 2.9 0
vertex 17.1 2.9 0
vertex 17.1 2.9 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 2.9 0
vertex 17.1 2.9 9.33
vertex 17.9 2.9 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 2.9 0
vertex 17.1 2.1 0
vertex 17.1 2.1 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 2.9 0
vertex 17.1 2.1 9.33
vertex 17.1 2.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 2.1 0
vertex 17.9 2.9 0
vertex 17.9 2.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 2.1 0
vertex 17.9 2.9 9.33
vertex 17.9 2.1 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 1.1 3.16
vertex 17.9 1.1 3.16
vertex 17.9 1.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 17.1 1.1 3.16
vertex 17.9 1.9 3.16
vertex 17.1 1.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 1.1 0
vertex 17.9 1.1 0
vertex 17.9 1.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 17.1 1.1 0
vertex 17.9 1.1 3.16
vertex 17.1 1.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 1.9 0
vertex 17.1 1.9 0
vertex 17.1 1.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 17.9 1.9 0
vertex 17.1 1.9 3.16
vertex 17.9 1.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 1.9 0
vertex 17.1 1.1 0
vertex 17.1 1.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 17.1 1.9 0
vertex 17.1 1.1 3.16
vertex 17.1 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 1.1 0
vertex 17.9 1.9 0
vertex 17.9 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 17.9 1.1 0
vertex 17.9 1.9 3.16
vertex 17.9 1.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 6.1 12.14
vertex 18.9 6.1 12.14
vertex 18.9 6.9 12.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 6.1 12.14
vertex 18.9 6.9 12.14
vertex 18.1 6.9 12.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 6.1 0
vertex 18.9 6.1 0
vertex 18.9 6.1 12.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 6.1 0
vertex 18.9 6.1 12.14
vertex 18.1 6.1 12.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 6.9 0
vertex 18.1 6.9 0
vertex 18.1 6.9 12.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 6.9 0
vertex 18.1 6.9 12.14
vertex 18.9 6.9 12.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 6.9 0
vertex 18.1 6.1 0
vertex 18.1 6.1 12.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 6.9 0
vertex 18.1 6.1 12.14
vertex 18.1 6.9 12.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 6.1 0
vertex 18.9 6.9 0
vertex 18.9 6.9 12.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 6.1 0
vertex 18.9 6.9 12.14
vertex 18.9 6.1 12.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 5.1 23.97
vertex 18.9 5.1 23.97
vertex 18.9 5.9 23.97
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 5.1 23.97
vertex 18.9 5.9 23.97
vertex 18.1 5.9 23.97
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 5.1 0
vertex 18.9 5.1 0
vertex 18.9 5.1 23.97
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 5.1 0
vertex 18.9 5.1 23.97
vertex 18.1 5.1 23.97
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 5.9 0
vertex 18.1 5.9 0
vertex 18.1 5.9 23.97
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 5.9 0
vertex 18.1 5.9 23.97
vertex 18.9 5.9 23.97
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 5.9 0
vertex 18.1 5.1 0
vertex 18.1 5.1 23.97
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 5.9 0
vertex 18.1 5.1 23.97
vertex 18.1 5.9 23.97
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 5.1 0
vertex 18.9 5.9 0
vertex 18.9 5.9 23.97
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 5.1 0
vertex 18.9 5.9 23.97
vertex 18.9 5.1 23.97
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 4.1 24.8
vertex 18.9 4.1 24.8
vertex 18.9 4.9 24.8
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 4.1 24.8
vertex 18.9 4.9 24.8
vertex 18.1 4.9 24.8
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 4.1 0
vertex 18.9 4.1 0
vertex 18.9 4.1 24.8
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 4.1 0
vertex 18.9 4.1 24.8
vertex 18.1 4.1 24.8
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 4.9 0
vertex 18.1 4.9 0
vertex 18.1 4.9 24.8
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 4.9 0
vertex 18.1 4.9 24.8
vertex 18.9 4.9 24.8
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 4.9 0
vertex 18.1 4.1 0
vertex 18.1 4.1 24.8
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 4.9 0
vertex 18.1 4.1 24.8
vertex 18.1 4.9 24.8
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 4.1 0
vertex 18.9 4.9 0
vertex 18.9 4.9 24.8
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 4.1 0
vertex 18.9 4.9 24.8
vertex 18.9 4.1 24.8
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 3.1 13.53
vertex 18.9 3.1 13.53
vertex 18.9 3.9 13.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 3.1 13.53
vertex 18.9 3.9 13.53
vertex 18.1 3.9 13.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 3.1 0
vertex 18.9 3.1 0
vertex 18.9 3.1 13.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 3.1 0
vertex 18.9 3.1 13.53
vertex 18.1 3.1 13.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 3.9 0
vertex 18.1 3.9 0
vertex 18.1 3.9 13.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 3.9 0
vertex 18.1 3.9 13.53
vertex 18.9 3.9 13.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 3.9 0
vertex 18.1 3.1 0
vertex 18.1 3.1 13.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 3.9 0
vertex 18.1 3.1 13.53
vertex 18.1 3.9 13.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 3.1 0
vertex 18.9 3.9 0
vertex 18.9 3.9 13.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 3.1 0
vertex 18.9 3.9 13.53
vertex 18.9 3.1 13.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 2.1 7.49
vertex 18.9 2.1 7.49
vertex 18.9 2.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 2.1 7.49
vertex 18.9 2.9 7.49
vertex 18.1 2.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 2.1 0
vertex 18.9 2.1 0
vertex 18.9 2.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 2.1 0
vertex 18.9 2.1 7.49
vertex 18.1 2.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 2.9 0
vertex 18.1 2.9 0
vertex 18.1 2.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 2.9 0
vertex 18.1 2.9 7.49
vertex 18.9 2.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 2.9 0
vertex 18.1 2.1 0
vertex 18.1 2.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 2.9 0
vertex 18.1 2.1 7.49
vertex 18.1 2.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 2.1 0
vertex 18.9 2.9 0
vertex 18.9 2.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 2.1 0
vertex 18.9 2.9 7.49
vertex 18.9 2.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 1.1 7.49
vertex 18.9 1.1 7.49
vertex 18.9 1.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 18.1 1.1 7.49
vertex 18.9 1.9 7.49
vertex 18.1 1.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 1.1 0
vertex 18.9 1.1 0
vertex 18.9 1.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 18.1 1.1 0
vertex 18.9 1.1 7.49
vertex 18.1 1.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 1.9 0
vertex 18.1 1.9 0
vertex 18.1 1.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 18.9 1.9 0
vertex 18.1 1.9 7.49
vertex 18.9 1.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 1.9 0
vertex 18.1 1.1 0
vertex 18.1 1.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 18.1 1.9 0
vertex 18.1 1.1 7.49
vertex 18.1 1.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 1.1 0
vertex 18.9 1.9 0
vertex 18.9 1.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 18.9 1.1 0
vertex 18.9 1.9 7.49
vertex 18.9 1.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 6.1 7.89
vertex 19.9 6.1 7.89
vertex 19.9 6.9 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 6.1 7.89
vertex 19.9 6.9 7.89
vertex 19.1 6.9 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 6.1 0
vertex 19.9 6.1 0
vertex 19.9 6.1 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 6.1 0
vertex 19.9 6.1 7.89
vertex 19.1 6.1 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 6.9 0
vertex 19.1 6.9 0
vertex 19.1 6.9 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 6.9 0
vertex 19.1 6.9 7.89
vertex 19.9 6.9 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 6.9 0
vertex 19.1 6.1 0
vertex 19.1 6.1 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 6.9 0
vertex 19.1 6.1 7.89
vertex 19.1 6.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 6.1 0
vertex 19.9 6.9 0
vertex 19.9 6.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 6.1 0
vertex 19.9 6.9 7.89
vertex 19.9 6.1 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 5.1 14.99
vertex 19.9 5.1 14.99
vertex 19.9 5.9 14.99
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 5.1 14.99
vertex 19.9 5.9 14.99
vertex 19.1 5.9 14.99
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 5.1 0
vertex 19.9 5.1 0
vertex 19.9 5.1 14.99
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 5.1 0
vertex 19.9 5.1 14.99
vertex 19.1 5.1 14.99
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 5.9 0
vertex 19.1 5.9 0
vertex 19.1 5.9 14.99
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 5.9 0
vertex 19.1 5.9 14.99
vertex 19.9 5.9 14.99
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 5.9 0
vertex 19.1 5.1 0
vertex 19.1 5.1 14.99
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 5.9 0
vertex 19.1 5.1 14.99
vertex 19.1 5.9 14.99
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 5.1 0
vertex 19.9 5.9 0
vertex 19.9 5.9 14.99
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 5.1 0
vertex 19.9 5.9 14.99
vertex 19.9 5.1 14.99
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 4.1 12.86
vertex 19.9 4.1 12.86
vertex 19.9 4.9 12.86
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 4.1 12.86
vertex 19.9 4.9 12.86
vertex 19.1 4.9 12.86
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 4.1 0
vertex 19.9 4.1 0
vertex 19.9 4.1 12.86
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 4.1 0
vertex 19.9 4.1 12.86
vertex 19.1 4.1 12.86
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 4.9 0
vertex 19.1 4.9 0
vertex 19.1 4.9 12.86
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 4.9 0
vertex 19.1 4.9 12.86
vertex 19.9 4.9 12.86
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 4.9 0
vertex 19.1 4.1 0
vertex 19.1 4.1 12.86
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 4.9 0
vertex 19.1 4.1 12.86
vertex 19.1 4.9 12.86
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 4.1 0
vertex 19.9 4.9 0
vertex 19.9 4.9 12.86
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 4.1 0
vertex 19.9 4.9 12.86
vertex 19.9 4.1 12.86
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 3.1 11.64
vertex 19.9 3.1 11.64
vertex 19.9 3.9 11.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 3.1 11.64
vertex 19.9 3.9 11.64
vertex 19.1 3.9 11.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 3.1 0
vertex 19.9 3.1 0
vertex 19.9 3.1 11.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 3.1 0
vertex 19.9 3.1 11.64
vertex 19.1 3.1 11.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 3.9 0
vertex 19.1 3.9 0
vertex 19.1 3.9 11.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 3.9 0
vertex 19.1 3.9 11.64
vertex 19.9 3.9 11.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 3.9 0
vertex 19.1 3.1 0
vertex 19.1 3.1 11.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 3.9 0
vertex 19.1 3.1 11.64
vertex 19.1 3.9 11.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 3.1 0
vertex 19.9 3.9 0
vertex 19.9 3.9 11.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 3.1 0
vertex 19.9 3.9 11.64
vertex 19.9 3.1 11.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 2.1 20.3
vertex 19.9 2.1 20.3
vertex 19.9 2.9 20.3
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 2.1 20.3
vertex 19.9 2.9 20.3
vertex 19.1 2.9 20.3
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 2.1 0
vertex 19.9 2.1 0
vertex 19.9 2.1 20.3
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 2.1 0
vertex 19.9 2.1 20.3
vertex 19.1 2.1 20.3
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 2.9 0
vertex 19.1 2.9 0
vertex 19.1 2.9 20.3
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 2.9 0
vertex 19.1 2.9 20.3
vertex 19.9 2.9 20.3
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 2.9 0
vertex 19.1 2.1 0
vertex 19.1 2.1 20.3
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 2.9 0
vertex 19.1 2.1 20.3
vertex 19.1 2.9 20.3
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 2.1 0
vertex 19.9 2.9 0
vertex 19.9 2.9 20.3
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 2.1 0
vertex 19.9 2.9 20.3
vertex 19.9 2.1 20.3
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 1.1 6.59
vertex 19.9 1.1 6.59
vertex 19.9 1.9 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 1.1 6.59
vertex 19.9 1.9 6.59
vertex 19.1 1.9 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 1.1 0
vertex 19.9 1.1 0
vertex 19.9 1.1 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 1.1 0
vertex 19.9 1.1 6.59
vertex 19.1 1.1 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 1.9 0
vertex 19.1 1.9 0
vertex 19.1 1.9 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 1.9 0
vertex 19.1 1.9 6.59
vertex 19.9 1.9 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 1.9 0
vertex 19.1 1.1 0
vertex 19.1 1.1 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 1.9 0
vertex 19.1 1.1 6.59
vertex 19.1 1.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 1.1 0
vertex 19.9 1.9 0
vertex 19.9 1.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 1.1 0
vertex 19.9 1.9 6.59
vertex 19.9 1.1 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 0.1 13.97
vertex 19.9 0.1 13.97
vertex 19.9 0.9 13.97
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 19.1 0.1 13.97
vertex 19.9 0.9 13.97
vertex 19.1 0.9 13.97
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 0.1 0
vertex 19.9 0.1 0
vertex 19.9 0.1 13.97
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 19.1 0.1 0
vertex 19.9 0.1 13.97
vertex 19.1 0.1 13.97
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 0.9 0
vertex 19.1 0.9 0
vertex 19.1 0.9 13.97
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 19.9 0.9 0
vertex 19.1 0.9 13.97
vertex 19.9 0.9 13.97
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 0.9 0
vertex 19.1 0.1 0
vertex 19.1 0.1 13.97
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 19.1 0.9 0
vertex 19.1 0.1 13.97
vertex 19.1 0.9 13.97
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 0.1 0
vertex 19.9 0.9 0
vertex 19.9 0.9 13.97
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 19.9 0.1 0
vertex 19.9 0.9 13.97
vertex 19.9 0.1 13.97
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 20.1 6.1 14.59
vertex 20.9 6.1 14.59
vertex 20.9 6.9 14.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 20.1 6.1 14.59
vertex 20.9 6.9 14.59
vertex 20.1 6.9 14.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 20.1 6.1 0
vertex 20.9 6.1 0
vertex 20.9 6.1 14.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 20.1 6.1 0
vertex 20.9 6.1 14.59
vertex 20.1 6.1 14.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 20.9 6.9 0
vertex 20.1 6.9 0
vertex 20.1 6.9 14.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 20.9 6.9 0
vertex 20.1 6.9 14.59
vertex 20.9 6.9 14.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 20.1 6.9 0
vertex 20.1 6.1 0
vertex 20.1 6.1 14.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 20.1 6.9 0
vertex 20.1 6.1 14.59
vertex 20.1 6.9 14.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 20.9 6.1 0
vertex 20.9 6.9 0
vertex 20.9 6.9 14.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 20.9 6.1 0
vertex 20.9 6.9 14.59
vertex 20.9 6.1 14.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 20.1 5.1 7.89
vertex 20.9 5.1 7.89
vertex 20.9 5.9 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 20.1 5.1 7.89
vertex 20.9 5.9 7.89
vertex 20.1 5.9 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 20.1 5.1 0
vertex 20.9 5.1 0
vertex 20.9 5.1 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 20.1 5.1 0
vertex 20.9 5.1 7.89
vertex 20.1 5.1 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 20.9 5.9 0
vertex 20.1 5.9 0
vertex 20.1 5.9 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 20.9 5.9 0
vertex 20.1 5.9 7.89
vertex 20.9 5.9 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 20.1 5.9 0
vertex 20.1 5.1 0
vertex 20.1 5.1 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 20.1 5.9 0
vertex 20.1 5.1 7.89
vertex 20.1 5.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 20.9 5.1 0
vertex 20.9 5.9 0
vertex 20.9 5.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 20.9 5.1 0
vertex 20.9 5.9 7.89
vertex 20.9 5.1 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 20.1 3.1 9.96
vertex 20.9 3.1 9.96
vertex 20.9 3.9 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 20.1 3.1 9.96
vertex 20.9 3.9 9.96
vertex 20.1 3.9 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 20.1 3.1 0
vertex 20.9 3.1 0
vertex 20.9 3.1 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 20.1 3.1 0
vertex 20.9 3.1 9.96
vertex 20.1 3.1 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 20.9 3.9 0
vertex 20.1 3.9 0
vertex 20.1 3.9 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 20.9 3.9 0
vertex 20.1 3.9 9.96
vertex 20.9 3.9 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 20.1 3.9 0
vertex 20.1 3.1 0
vertex 20.1 3.1 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 20.1 3.9 0
vertex 20.1 3.1 9.96
vertex 20.1 3.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 20.9 3.1 0
vertex 20.9 3.9 0
vertex 20.9 3.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 20.9 3.1 0
vertex 20.9 3.9 9.96
vertex 20.9 3.1 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 20.1 2.1 8.99
vertex 20.9 2.1 8.99
vertex 20.9 2.9 8.99
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 20.1 2.1 8.99
vertex 20.9 2.9 8.99
vertex 20.1 2.9 8.99
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 20.1 2.1 0
vertex 20.9 2.1 0
vertex 20.9 2.1 8.99
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 20.1 2.1 0
vertex 20.9 2.1 8.99
vertex 20.1 2.1 8.99
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 20.9 2.9 0
vertex 20.1 2.9 0
vertex 20.1 2.9 8.99
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 20.9 2.9 0
vertex 20.1 2.9 8.99
vertex 20.9 2.9 8.99
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 20.1 2.9 0
vertex 20.1 2.1 0
vertex 20.1 2.1 8.99
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 20.1 2.9 0
vertex 20.1 2.1 8.99
vertex 20.1 2.9 8.99
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 20.9 2.1 0
vertex 20.9 2.9 0
vertex 20.9 2.9 8.99
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 20.9 2.1 0
vertex 20.9 2.9 8.99
vertex 20.9 2.1 8.99
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 21.1 6.1 4.9
vertex 21.9 6.1 4.9
vertex 21.9 6.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 21.1 6.1 4.9
vertex 21.9 6.9 4.9
vertex 21.1 6.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 21.1 6.1 0
vertex 21.9 6.1 0
vertex 21.9 6.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 21.1 6.1 0
vertex 21.9 6.1 4.9
vertex 21.1 6.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 21.9 6.9 0
vertex 21.1 6.9 0
vertex 21.1 6.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 21.9 6.9 0
vertex 21.1 6.9 4.9
vertex 21.9 6.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 21.1 6.9 0
vertex 21.1 6.1 0
vertex 21.1 6.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 21.1 6.9 0
vertex 21.1 6.1 4.9
vertex 21.1 6.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 21.9 6.1 0
vertex 21.9 6.9 0
vertex 21.9 6.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 21.9 6.1 0
vertex 21.9 6.9 4.9
vertex 21.9 6.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 21.1 2.1 7.49
vertex 21.9 2.1 7.49
vertex 21.9 2.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 21.1 2.1 7.49
vertex 21.9 2.9 7.49
vertex 21.1 2.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 21.1 2.1 0
vertex 21.9 2.1 0
vertex 21.9 2.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 21.1 2.1 0
vertex 21.9 2.1 7.49
vertex 21.1 2.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 21.9 2.9 0
vertex 21.1 2.9 0
vertex 21.1 2.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 21.9 2.9 0
vertex 21.1 2.9 7.49
vertex 21.9 2.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 21.1 2.9 0
vertex 21.1 2.1 0
vertex 21.1 2.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 21.1 2.9 0
vertex 21.1 2.1 7.49
vertex 21.1 2.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 21.9 2.1 0
vertex 21.9 2.9 0
vertex 21.9 2.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 21.9 2.1 0
vertex 21.9 2.9 7.49
vertex 21.9 2.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 21.1 1.1 5.53
vertex 21.9 1.1 5.53
vertex 21.9 1.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 21.1 1.1 5.53
vertex 21.9 1.9 5.53
vertex 21.1 1.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 21.1 1.1 0
vertex 21.9 1.1 0
vertex 21.9 1.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 21.1 1.1 0
vertex 21.9 1.1 5.53
vertex 21.1 1.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 21.9 1.9 0
vertex 21.1 1.9 0
vertex 21.1 1.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 21.9 1.9 0
vertex 21.1 1.9 5.53
vertex 21.9 1.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 21.1 1.9 0
vertex 21.1 1.1 0
vertex 21.1 1.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 21.1 1.9 0
vertex 21.1 1.1 5.53
vertex 21.1 1.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 21.9 1.1 0
vertex 21.9 1.9 0
vertex 21.9 1.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 21.9 1.1 0
vertex 21.9 1.9 5.53
vertex 21.9 1.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 22.1 6.1 9.33
vertex 22.9 6.1 9.33
vertex 22.9 6.9 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 22.1 6.1 9.33
vertex 22.9 6.9 9.33
vertex 22.1 6.9 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 22.1 6.1 0
vertex 22.9 6.1 0
vertex 22.9 6.1 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 22.1 6.1 0
vertex 22.9 6.1 9.33
vertex 22.1 6.1 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 22.9 6.9 0
vertex 22.1 6.9 0
vertex 22.1 6.9 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 22.9 6.9 0
vertex 22.1 6.9 9.33
vertex 22.9 6.9 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 22.1 6.9 0
vertex 22.1 6.1 0
vertex 22.1 6.1 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 22.1 6.9 0
vertex 22.1 6.1 9.33
vertex 22.1 6.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 22.9 6.1 0
vertex 22.9 6.9 0
vertex 22.9 6.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 22.9 6.1 0
vertex 22.9 6.9 9.33
vertex 22.9 6.1 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 22.1 5.1 6.59
vertex 22.9 5.1 6.59
vertex 22.9 5.9 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 22.1 5.1 6.59
vertex 22.9 5.9 6.59
vertex 22.1 5.9 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 22.1 5.1 0
vertex 22.9 5.1 0
vertex 22.9 5.1 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 22.1 5.1 0
vertex 22.9 5.1 6.59
vertex 22.1 5.1 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 22.9 5.9 0
vertex 22.1 5.9 0
vertex 22.1 5.9 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 22.9 5.9 0
vertex 22.1 5.9 6.59
vertex 22.9 5.9 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 22.1 5.9 0
vertex 22.1 5.1 0
vertex 22.1 5.1 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 22.1 5.9 0
vertex 22.1 5.1 6.59
vertex 22.1 5.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 22.9 5.1 0
vertex 22.9 5.9 0
vertex 22.9 5.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 22.9 5.1 0
vertex 22.9 5.9 6.59
vertex 22.9 5.1 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 22.1 4.1 9.33
vertex 22.9 4.1 9.33
vertex 22.9 4.9 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 22.1 4.1 9.33
vertex 22.9 4.9 9.33
vertex 22.1 4.9 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 22.1 4.1 0
vertex 22.9 4.1 0
vertex 22.9 4.1 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 22.1 4.1 0
vertex 22.9 4.1 9.33
vertex 22.1 4.1 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 22.9 4.9 0
vertex 22.1 4.9 0
vertex 22.1 4.9 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 22.9 4.9 0
vertex 22.1 4.9 9.33
vertex 22.9 4.9 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 22.1 4.9 0
vertex 22.1 4.1 0
vertex 22.1 4.1 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 22.1 4.9 0
vertex 22.1 4.1 9.33
vertex 22.1 4.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 22.9 4.1 0
vertex 22.9 4.9 0
vertex 22.9 4.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 22.9 4.1 0
vertex 22.9 4.9 9.33
vertex 22.9 4.1 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 23.1 6.1 3.16
vertex 23.9 6.1 3.16
vertex 23.9 6.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 23.1 6.1 3.16
vertex 23.9 6.9 3.16
vertex 23.1 6.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 23.1 6.1 0
vertex 23.9 6.1 0
vertex 23.9 6.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 23.1 6.1 0
vertex 23.9 6.1 3.16
vertex 23.1 6.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 23.9 6.9 0
vertex 23.1 6.9 0
vertex 23.1 6.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 23.9 6.9 0
vertex 23.1 6.9 3.16
vertex 23.9 6.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 23.1 6.9 0
vertex 23.1 6.1 0
vertex 23.1 6.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 23.1 6.9 0
vertex 23.1 6.1 3.16
vertex 23.1 6.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 23.9 6.1 0
vertex 23.9 6.9 0
vertex 23.9 6.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 23.9 6.1 0
vertex 23.9 6.9 3.16
vertex 23.9 6.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 24.1 5.1 4.14
vertex 24.9 5.1 4.14
vertex 24.9 5.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 24.1 5.1 4.14
vertex 24.9 5.9 4.14
vertex 24.1 5.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 24.1 5.1 0
vertex 24.9 5.1 0
vertex 24.9 5.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 24.1 5.1 0
vertex 24.9 5.1 4.14
vertex 24.1 5.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 24.9 5.9 0
vertex 24.1 5.9 0
vertex 24.1 5.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 24.9 5.9 0
vertex 24.1 5.9 4.14
vertex 24.9 5.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 24.1 5.9 0
vertex 24.1 5.1 0
vertex 24.1 5.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 24.1 5.9 0
vertex 24.1 5.1 4.14
vertex 24.1 5.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 24.9 5.1 0
vertex 24.9 5.9 0
vertex 24.9 5.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 24.9 5.1 0
vertex 24.9 5.9 4.14
vertex 24.9 5.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 24.1 1.1 3.16
vertex 24.9 1.1 3.16
vertex 24.9 1.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 24.1 1.1 3.16
vertex 24.9 1.9 3.16
vertex 24.1 1.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 24.1 1.1 0
vertex 24.9 1.1 0
vertex 24.9 1.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 24.1 1.1 0
vertex 24.9 1.1 3.16
vertex 24.1 1.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 24.9 1.9 0
vertex 24.1 1.9 0
vertex 24.1 1.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 24.9 1.9 0
vertex 24.1 1.9 3.16
vertex 24.9 1.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 24.1 1.9 0
vertex 24.1 1.1 0
vertex 24.1 1.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 24.1 1.9 0
vertex 24.1 1.1 3.16
vertex 24.1 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 24.9 1.1 0
vertex 24.9 1.9 0
vertex 24.9 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 24.9 1.1 0
vertex 24.9 1.9 3.16
vertex 24.9 1.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 25.1 4.1 11.38
vertex 25.9 4.1 11.38
vertex 25.9 4.9 11.38
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 25.1 4.1 11.38
vertex 25.9 4.9 11.38
vertex 25.1 4.9 11.38
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 25.1 4.1 0
vertex 25.9 4.1 0
vertex 25.9 4.1 11.38
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 25.1 4.1 0
vertex 25.9 4.1 11.38
vertex 25.1 4.1 11.38
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 25.9 4.9 0
vertex 25.1 4.9 0
vertex 25.1 4.9 11.38
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 25.9 4.9 0
vertex 25.1 4.9 11.38
vertex 25.9 4.9 11.38
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 25.1 4.9 0
vertex 25.1 4.1 0
vertex 25.1 4.1 11.38
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 25.1 4.9 0
vertex 25.1 4.1 11.38
vertex 25.1 4.9 11.38
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 25.9 4.1 0
vertex 25.9 4.9 0
vertex 25.9 4.9 11.38
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 25.9 4.1 0
vertex 25.9 4.9 11.38
vertex 25.9 4.1 11.38
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 25.1 3.1 6.09
vertex 25.9 3.1 6.09
vertex 25.9 3.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 25.1 3.1 6.09
vertex 25.9 3.9 6.09
vertex 25.1 3.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 25.1 3.1 0
vertex 25.9 3.1 0
vertex 25.9 3.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 25.1 3.1 0
vertex 25.9 3.1 6.09
vertex 25.1 3.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 25.9 3.9 0
vertex 25.1 3.9 0
vertex 25.1 3.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 25.9 3.9 0
vertex 25.1 3.9 6.09
vertex 25.9 3.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 25.1 3.9 0
vertex 25.1 3.1 0
vertex 25.1 3.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 25.1 3.9 0
vertex 25.1 3.1 6.09
vertex 25.1 3.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 25.9 3.1 0
vertex 25.9 3.9 0
vertex 25.9 3.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 25.9 3.1 0
vertex 25.9 3.9 6.09
vertex 25.9 3.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 25.1 1.1 8.64
vertex 25.9 1.1 8.64
vertex 25.9 1.9 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 25.1 1.1 8.64
vertex 25.9 1.9 8.64
vertex 25.1 1.9 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 25.1 1.1 0
vertex 25.9 1.1 0
vertex 25.9 1.1 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 25.1 1.1 0
vertex 25.9 1.1 8.64
vertex 25.1 1.1 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 25.9 1.9 0
vertex 25.1 1.9 0
vertex 25.1 1.9 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 25.9 1.9 0
vertex 25.1 1.9 8.64
vertex 25.9 1.9 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 25.1 1.9 0
vertex 25.1 1.1 0
vertex 25.1 1.1 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 25.1 1.9 0
vertex 25.1 1.1 8.64
vertex 25.1 1.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 25.9 1.1 0
vertex 25.9 1.9 0
vertex 25.9 1.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 25.9 1.1 0
vertex 25.9 1.9 8.64
vertex 25.9 1.1 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 25.1 0.1 4.9
vertex 25.9 0.1 4.9
vertex 25.9 0.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 25.1 0.1 4.9
vertex 25.9 0.9 4.9
vertex 25.1 0.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 25.1 0.1 0
vertex 25.9 0.1 0
vertex 25.9 0.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 25.1 0.1 0
vertex 25.9 0.1 4.9
vertex 25.1 0.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 25.9 0.9 0
vertex 25.1 0.9 0
vertex 25.1 0.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 25.9 0.9 0
vertex 25.1 0.9 4.9
vertex 25.9 0.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 25.1 0.9 0
vertex 25.1 0.1 0
vertex 25.1 0.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 25.1 0.9 0
vertex 25.1 0.1 4.9
vertex 25.1 0.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 25.9 0.1 0
vertex 25.9 0.9 0
vertex 25.9 0.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 25.9 0.1 0
vertex 25.9 0.9 4.9
vertex 25.9 0.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 6.1 6.09
vertex 26.9 6.1 6.09
vertex 26.9 6.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 6.1 6.09
vertex 26.9 6.9 6.09
vertex 26.1 6.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 6.1 0
vertex 26.9 6.1 0
vertex 26.9 6.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 6.1 0
vertex 26.9 6.1 6.09
vertex 26.1 6.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 6.9 0
vertex 26.1 6.9 0
vertex 26.1 6.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 6.9 0
vertex 26.1 6.9 6.09
vertex 26.9 6.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 6.9 0
vertex 26.1 6.1 0
vertex 26.1 6.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 6.9 0
vertex 26.1 6.1 6.09
vertex 26.1 6.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 6.1 0
vertex 26.9 6.9 0
vertex 26.9 6.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 6.1 0
vertex 26.9 6.9 6.09
vertex 26.9 6.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 5.1 9.65
vertex 26.9 5.1 9.65
vertex 26.9 5.9 9.65
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 5.1 9.65
vertex 26.9 5.9 9.65
vertex 26.1 5.9 9.65
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 5.1 0
vertex 26.9 5.1 0
vertex 26.9 5.1 9.65
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 5.1 0
vertex 26.9 5.1 9.65
vertex 26.1 5.1 9.65
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 5.9 0
vertex 26.1 5.9 0
vertex 26.1 5.9 9.65
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 5.9 0
vertex 26.1 5.9 9.65
vertex 26.9 5.9 9.65
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 5.9 0
vertex 26.1 5.1 0
vertex 26.1 5.1 9.65
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 5.9 0
vertex 26.1 5.1 9.65
vertex 26.1 5.9 9.65
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 5.1 0
vertex 26.9 5.9 0
vertex 26.9 5.9 9.65
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 5.1 0
vertex 26.9 5.9 9.65
vertex 26.9 5.1 9.65
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 4.1 6.59
vertex 26.9 4.1 6.59
vertex 26.9 4.9 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 4.1 6.59
vertex 26.9 4.9 6.59
vertex 26.1 4.9 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 4.1 0
vertex 26.9 4.1 0
vertex 26.9 4.1 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 4.1 0
vertex 26.9 4.1 6.59
vertex 26.1 4.1 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 4.9 0
vertex 26.1 4.9 0
vertex 26.1 4.9 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 4.9 0
vertex 26.1 4.9 6.59
vertex 26.9 4.9 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 4.9 0
vertex 26.1 4.1 0
vertex 26.1 4.1 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 4.9 0
vertex 26.1 4.1 6.59
vertex 26.1 4.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 4.1 0
vertex 26.9 4.9 0
vertex 26.9 4.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 4.1 0
vertex 26.9 4.9 6.59
vertex 26.9 4.1 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 3.1 9.33
vertex 26.9 3.1 9.33
vertex 26.9 3.9 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 3.1 9.33
vertex 26.9 3.9 9.33
vertex 26.1 3.9 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 3.1 0
vertex 26.9 3.1 0
vertex 26.9 3.1 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 3.1 0
vertex 26.9 3.1 9.33
vertex 26.1 3.1 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 3.9 0
vertex 26.1 3.9 0
vertex 26.1 3.9 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 3.9 0
vertex 26.1 3.9 9.33
vertex 26.9 3.9 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 3.9 0
vertex 26.1 3.1 0
vertex 26.1 3.1 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 3.9 0
vertex 26.1 3.1 9.33
vertex 26.1 3.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 3.1 0
vertex 26.9 3.9 0
vertex 26.9 3.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 3.1 0
vertex 26.9 3.9 9.33
vertex 26.9 3.1 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 2.1 8.64
vertex 26.9 2.1 8.64
vertex 26.9 2.9 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 26.1 2.1 8.64
vertex 26.9 2.9 8.64
vertex 26.1 2.9 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 2.1 0
vertex 26.9 2.1 0
vertex 26.9 2.1 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 26.1 2.1 0
vertex 26.9 2.1 8.64
vertex 26.1 2.1 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 2.9 0
vertex 26.1 2.9 0
vertex 26.1 2.9 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 26.9 2.9 0
vertex 26.1 2.9 8.64
vertex 26.9 2.9 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 2.9 0
vertex 26.1 2.1 0
vertex 26.1 2.1 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 26.1 2.9 0
vertex 26.1 2.1 8.64
vertex 26.1 2.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 2.1 0
vertex 26.9 2.9 0
vertex 26.9 2.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 26.9 2.1 0
vertex 26.9 2.9 8.64
vertex 26.9 2.1 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 27.1 6.1 4.9
vertex 27.9 6.1 4.9
vertex 27.9 6.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 27.1 6.1 4.9
vertex 27.9 6.9 4.9
vertex 27.1 6.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 27.1 6.1 0
vertex 27.9 6.1 0
vertex 27.9 6.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 27.1 6.1 0
vertex 27.9 6.1 4.9
vertex 27.1 6.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 27.9 6.9 0
vertex 27.1 6.9 0
vertex 27.1 6.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 27.9 6.9 0
vertex 27.1 6.9 4.9
vertex 27.9 6.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 27.1 6.9 0
vertex 27.1 6.1 0
vertex 27.1 6.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 27.1 6.9 0
vertex 27.1 6.1 4.9
vertex 27.1 6.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 27.9 6.1 0
vertex 27.9 6.9 0
vertex 27.9 6.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 27.9 6.1 0
vertex 27.9 6.9 4.9
vertex 27.9 6.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 27.1 5.1 10.83
vertex 27.9 5.1 10.83
vertex 27.9 5.9 10.83
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 27.1 5.1 10.83
vertex 27.9 5.9 10.83
vertex 27.1 5.9 10.83
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 27.1 5.1 0
vertex 27.9 5.1 0
vertex 27.9 5.1 10.83
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 27.1 5.1 0
vertex 27.9 5.1 10.83
vertex 27.1 5.1 10.83
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 27.9 5.9 0
vertex 27.1 5.9 0
vertex 27.1 5.9 10.83
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 27.9 5.9 0
vertex 27.1 5.9 10.83
vertex 27.9 5.9 10.83
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 27.1 5.9 0
vertex 27.1 5.1 0
vertex 27.1 5.1 10.83
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 27.1 5.9 0
vertex 27.1 5.1 10.83
vertex 27.1 5.9 10.83
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 27.9 5.1 0
vertex 27.9 5.9 0
vertex 27.9 5.9 10.83
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 27.9 5.1 0
vertex 27.9 5.9 10.83
vertex 27.9 5.1 10.83
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 27.1 4.1 3.16
vertex 27.9 4.1 3.16
vertex 27.9 4.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 27.1 4.1 3.16
vertex 27.9 4.9 3.16
vertex 27.1 4.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 27.1 4.1 0
vertex 27.9 4.1 0
vertex 27.9 4.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 27.1 4.1 0
vertex 27.9 4.1 3.16
vertex 27.1 4.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 27.9 4.9 0
vertex 27.1 4.9 0
vertex 27.1 4.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 27.9 4.9 0
vertex 27.1 4.9 3.16
vertex 27.9 4.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 27.1 4.9 0
vertex 27.1 4.1 0
vertex 27.1 4.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 27.1 4.9 0
vertex 27.1 4.1 3.16
vertex 27.1 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 27.9 4.1 0
vertex 27.9 4.9 0
vertex 27.9 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 27.9 4.1 0
vertex 27.9 4.9 3.16
vertex 27.9 4.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 27.1 3.1 6.09
vertex 27.9 3.1 6.09
vertex 27.9 3.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 27.1 3.1 6.09
vertex 27.9 3.9 6.09
vertex 27.1 3.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 27.1 3.1 0
vertex 27.9 3.1 0
vertex 27.9 3.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 27.1 3.1 0
vertex 27.9 3.1 6.09
vertex 27.1 3.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 27.9 3.9 0
vertex 27.1 3.9 0
vertex 27.1 3.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 27.9 3.9 0
vertex 27.1 3.9 6.09
vertex 27.9 3.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 27.1 3.9 0
vertex 27.1 3.1 0
vertex 27.1 3.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 27.1 3.9 0
vertex 27.1 3.1 6.09
vertex 27.1 3.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 27.9 3.1 0
vertex 27.9 3.9 0
vertex 27.9 3.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 27.9 3.1 0
vertex 27.9 3.9 6.09
vertex 27.9 3.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 6.1 8.28
vertex 28.9 6.1 8.28
vertex 28.9 6.9 8.28
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 6.1 8.28
vertex 28.9 6.9 8.28
vertex 28.1 6.9 8.28
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 6.1 0
vertex 28.9 6.1 0
vertex 28.9 6.1 8.28
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 6.1 0
vertex 28.9 6.1 8.28
vertex 28.1 6.1 8.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 6.9 0
vertex 28.1 6.9 0
vertex 28.1 6.9 8.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 6.9 0
vertex 28.1 6.9 8.28
vertex 28.9 6.9 8.28
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 6.9 0
vertex 28.1 6.1 0
vertex 28.1 6.1 8.28
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 6.9 0
vertex 28.1 6.1 8.28
vertex 28.1 6.9 8.28
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 6.1 0
vertex 28.9 6.9 0
vertex 28.9 6.9 8.28
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 6.1 0
vertex 28.9 6.9 8.28
vertex 28.9 6.1 8.28
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 5.1 5.53
vertex 28.9 5.1 5.53
vertex 28.9 5.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 5.1 5.53
vertex 28.9 5.9 5.53
vertex 28.1 5.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 5.1 0
vertex 28.9 5.1 0
vertex 28.9 5.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 5.1 0
vertex 28.9 5.1 5.53
vertex 28.1 5.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 5.9 0
vertex 28.1 5.9 0
vertex 28.1 5.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 5.9 0
vertex 28.1 5.9 5.53
vertex 28.9 5.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 5.9 0
vertex 28.1 5.1 0
vertex 28.1 5.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 5.9 0
vertex 28.1 5.1 5.53
vertex 28.1 5.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 5.1 0
vertex 28.9 5.9 0
vertex 28.9 5.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 5.1 0
vertex 28.9 5.9 5.53
vertex 28.9 5.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 4.1 7.06
vertex 28.9 4.1 7.06
vertex 28.9 4.9 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 4.1 7.06
vertex 28.9 4.9 7.06
vertex 28.1 4.9 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 4.1 0
vertex 28.9 4.1 0
vertex 28.9 4.1 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 4.1 0
vertex 28.9 4.1 7.06
vertex 28.1 4.1 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 4.9 0
vertex 28.1 4.9 0
vertex 28.1 4.9 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 4.9 0
vertex 28.1 4.9 7.06
vertex 28.9 4.9 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 4.9 0
vertex 28.1 4.1 0
vertex 28.1 4.1 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 4.9 0
vertex 28.1 4.1 7.06
vertex 28.1 4.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 4.1 0
vertex 28.9 4.9 0
vertex 28.9 4.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 4.1 0
vertex 28.9 4.9 7.06
vertex 28.9 4.1 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 3.1 4.14
vertex 28.9 3.1 4.14
vertex 28.9 3.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 3.1 4.14
vertex 28.9 3.9 4.14
vertex 28.1 3.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 3.1 0
vertex 28.9 3.1 0
vertex 28.9 3.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 3.1 0
vertex 28.9 3.1 4.14
vertex 28.1 3.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 3.9 0
vertex 28.1 3.9 0
vertex 28.1 3.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 3.9 0
vertex 28.1 3.9 4.14
vertex 28.9 3.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 3.9 0
vertex 28.1 3.1 0
vertex 28.1 3.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 3.9 0
vertex 28.1 3.1 4.14
vertex 28.1 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 3.1 0
vertex 28.9 3.9 0
vertex 28.9 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 3.1 0
vertex 28.9 3.9 4.14
vertex 28.9 3.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 2.1 3.16
vertex 28.9 2.1 3.16
vertex 28.9 2.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 28.1 2.1 3.16
vertex 28.9 2.9 3.16
vertex 28.1 2.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 2.1 0
vertex 28.9 2.1 0
vertex 28.9 2.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 28.1 2.1 0
vertex 28.9 2.1 3.16
vertex 28.1 2.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 2.9 0
vertex 28.1 2.9 0
vertex 28.1 2.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 28.9 2.9 0
vertex 28.1 2.9 3.16
vertex 28.9 2.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 2.9 0
vertex 28.1 2.1 0
vertex 28.1 2.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 28.1 2.9 0
vertex 28.1 2.1 3.16
vertex 28.1 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 2.1 0
vertex 28.9 2.9 0
vertex 28.9 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 28.9 2.1 0
vertex 28.9 2.9 3.16
vertex 28.9 2.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 29.1 1.1 3.16
vertex 29.9 1.1 3.16
vertex 29.9 1.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 29.1 1.1 3.16
vertex 29.9 1.9 3.16
vertex 29.1 1.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 29.1 1.1 0
vertex 29.9 1.1 0
vertex 29.9 1.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 29.1 1.1 0
vertex 29.9 1.1 3.16
vertex 29.1 1.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 29.9 1.9 0
vertex 29.1 1.9 0
vertex 29.1 1.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 29.9 1.9 0
vertex 29.1 1.9 3.16
vertex 29.9 1.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 29.1 1.9 0
vertex 29.1 1.1 0
vertex 29.1 1.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 29.1 1.9 0
vertex 29.1 1.1 3.16
vertex 29.1 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 29.9 1.1 0
vertex 29.9 1.9 0
vertex 29.9 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 29.9 1.1 0
vertex 29.9 1.9 3.16
vertex 29.9 1.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 6.1 12.39
vertex 30.9 6.1 12.39
vertex 30.9 6.9 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 6.1 12.39
vertex 30.9 6.9 12.39
vertex 30.1 6.9 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 6.1 0
vertex 30.9 6.1 0
vertex 30.9 6.1 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 6.1 0
vertex 30.9 6.1 12.39
vertex 30.1 6.1 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 6.9 0
vertex 30.1 6.9 0
vertex 30.1 6.9 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 6.9 0
vertex 30.1 6.9 12.39
vertex 30.9 6.9 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 6.9 0
vertex 30.1 6.1 0
vertex 30.1 6.1 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 6.9 0
vertex 30.1 6.1 12.39
vertex 30.1 6.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 6.1 0
vertex 30.9 6.9 0
vertex 30.9 6.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 6.1 0
vertex 30.9 6.9 12.39
vertex 30.9 6.1 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 5.1 3.16
vertex 30.9 5.1 3.16
vertex 30.9 5.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 5.1 3.16
vertex 30.9 5.9 3.16
vertex 30.1 5.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 5.1 0
vertex 30.9 5.1 0
vertex 30.9 5.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 5.1 0
vertex 30.9 5.1 3.16
vertex 30.1 5.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 5.9 0
vertex 30.1 5.9 0
vertex 30.1 5.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 5.9 0
vertex 30.1 5.9 3.16
vertex 30.9 5.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 5.9 0
vertex 30.1 5.1 0
vertex 30.1 5.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 5.9 0
vertex 30.1 5.1 3.16
vertex 30.1 5.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 5.1 0
vertex 30.9 5.9 0
vertex 30.9 5.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 5.1 0
vertex 30.9 5.9 3.16
vertex 30.9 5.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 4.1 3.16
vertex 30.9 4.1 3.16
vertex 30.9 4.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 4.1 3.16
vertex 30.9 4.9 3.16
vertex 30.1 4.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 4.1 0
vertex 30.9 4.1 0
vertex 30.9 4.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 4.1 0
vertex 30.9 4.1 3.16
vertex 30.1 4.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 4.9 0
vertex 30.1 4.9 0
vertex 30.1 4.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 4.9 0
vertex 30.1 4.9 3.16
vertex 30.9 4.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 4.9 0
vertex 30.1 4.1 0
vertex 30.1 4.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 4.9 0
vertex 30.1 4.1 3.16
vertex 30.1 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 4.1 0
vertex 30.9 4.9 0
vertex 30.9 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 4.1 0
vertex 30.9 4.9 3.16
vertex 30.9 4.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 2.1 6.09
vertex 30.9 2.1 6.09
vertex 30.9 2.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 2.1 6.09
vertex 30.9 2.9 6.09
vertex 30.1 2.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 2.1 0
vertex 30.9 2.1 0
vertex 30.9 2.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 2.1 0
vertex 30.9 2.1 6.09
vertex 30.1 2.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 2.9 0
vertex 30.1 2.9 0
vertex 30.1 2.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 2.9 0
vertex 30.1 2.9 6.09
vertex 30.9 2.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 2.9 0
vertex 30.1 2.1 0
vertex 30.1 2.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 2.9 0
vertex 30.1 2.1 6.09
vertex 30.1 2.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 2.1 0
vertex 30.9 2.9 0
vertex 30.9 2.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 2.1 0
vertex 30.9 2.9 6.09
vertex 30.9 2.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 1.1 3.16
vertex 30.9 1.1 3.16
vertex 30.9 1.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 1.1 3.16
vertex 30.9 1.9 3.16
vertex 30.1 1.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 1.1 0
vertex 30.9 1.1 0
vertex 30.9 1.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 1.1 0
vertex 30.9 1.1 3.16
vertex 30.1 1.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 1.9 0
vertex 30.1 1.9 0
vertex 30.1 1.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 1.9 0
vertex 30.1 1.9 3.16
vertex 30.9 1.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 1.9 0
vertex 30.1 1.1 0
vertex 30.1 1.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 1.9 0
vertex 30.1 1.1 3.16
vertex 30.1 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 1.1 0
vertex 30.9 1.9 0
vertex 30.9 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 1.1 0
vertex 30.9 1.9 3.16
vertex 30.9 1.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 0.1 8.28
vertex 30.9 0.1 8.28
vertex 30.9 0.9 8.28
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 30.1 0.1 8.28
vertex 30.9 0.9 8.28
vertex 30.1 0.9 8.28
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 0.1 0
vertex 30.9 0.1 0
vertex 30.9 0.1 8.28
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 30.1 0.1 0
vertex 30.9 0.1 8.28
vertex 30.1 0.1 8.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 0.9 0
vertex 30.1 0.9 0
vertex 30.1 0.9 8.28
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 30.9 0.9 0
vertex 30.1 0.9 8.28
vertex 30.9 0.9 8.28
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 0.9 0
vertex 30.1 0.1 0
vertex 30.1 0.1 8.28
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 30.1 0.9 0
vertex 30.1 0.1 8.28
vertex 30.1 0.9 8.28
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 0.1 0
vertex 30.9 0.9 0
vertex 30.9 0.9 8.28
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 30.9 0.1 0
vertex 30.9 0.9 8.28
vertex 30.9 0.1 8.28
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 6.1 12.62
vertex 31.9 6.1 12.62
vertex 31.9 6.9 12.62
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 6.1 12.62
vertex 31.9 6.9 12.62
vertex 31.1 6.9 12.62
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 6.1 0
vertex 31.9 6.1 0
vertex 31.9 6.1 12.62
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 6.1 0
vertex 31.9 6.1 12.62
vertex 31.1 6.1 12.62
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 6.9 0
vertex 31.1 6.9 0
vertex 31.1 6.9 12.62
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 6.9 0
vertex 31.1 6.9 12.62
vertex 31.9 6.9 12.62
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 6.9 0
vertex 31.1 6.1 0
vertex 31.1 6.1 12.62
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 6.9 0
vertex 31.1 6.1 12.62
vertex 31.1 6.9 12.62
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 6.1 0
vertex 31.9 6.9 0
vertex 31.9 6.9 12.62
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 6.1 0
vertex 31.9 6.9 12.62
vertex 31.9 6.1 12.62
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 5.1 8.64
vertex 31.9 5.1 8.64
vertex 31.9 5.9 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 5.1 8.64
vertex 31.9 5.9 8.64
vertex 31.1 5.9 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 5.1 0
vertex 31.9 5.1 0
vertex 31.9 5.1 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 5.1 0
vertex 31.9 5.1 8.64
vertex 31.1 5.1 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 5.9 0
vertex 31.1 5.9 0
vertex 31.1 5.9 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 5.9 0
vertex 31.1 5.9 8.64
vertex 31.9 5.9 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 5.9 0
vertex 31.1 5.1 0
vertex 31.1 5.1 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 5.9 0
vertex 31.1 5.1 8.64
vertex 31.1 5.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 5.1 0
vertex 31.9 5.9 0
vertex 31.9 5.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 5.1 0
vertex 31.9 5.9 8.64
vertex 31.9 5.1 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 4.1 3.16
vertex 31.9 4.1 3.16
vertex 31.9 4.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 4.1 3.16
vertex 31.9 4.9 3.16
vertex 31.1 4.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 4.1 0
vertex 31.9 4.1 0
vertex 31.9 4.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 4.1 0
vertex 31.9 4.1 3.16
vertex 31.1 4.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 4.9 0
vertex 31.1 4.9 0
vertex 31.1 4.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 4.9 0
vertex 31.1 4.9 3.16
vertex 31.9 4.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 4.9 0
vertex 31.1 4.1 0
vertex 31.1 4.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 4.9 0
vertex 31.1 4.1 3.16
vertex 31.1 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 4.1 0
vertex 31.9 4.9 0
vertex 31.9 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 4.1 0
vertex 31.9 4.9 3.16
vertex 31.9 4.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 3.1 9.96
vertex 31.9 3.1 9.96
vertex 31.9 3.9 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 3.1 9.96
vertex 31.9 3.9 9.96
vertex 31.1 3.9 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 3.1 0
vertex 31.9 3.1 0
vertex 31.9 3.1 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 3.1 0
vertex 31.9 3.1 9.96
vertex 31.1 3.1 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 3.9 0
vertex 31.1 3.9 0
vertex 31.1 3.9 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 3.9 0
vertex 31.1 3.9 9.96
vertex 31.9 3.9 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 3.9 0
vertex 31.1 3.1 0
vertex 31.1 3.1 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 3.9 0
vertex 31.1 3.1 9.96
vertex 31.1 3.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 3.1 0
vertex 31.9 3.9 0
vertex 31.9 3.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 3.1 0
vertex 31.9 3.9 9.96
vertex 31.9 3.1 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 1.1 4.9
vertex 31.9 1.1 4.9
vertex 31.9 1.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 31.1 1.1 4.9
vertex 31.9 1.9 4.9
vertex 31.1 1.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 1.1 0
vertex 31.9 1.1 0
vertex 31.9 1.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 31.1 1.1 0
vertex 31.9 1.1 4.9
vertex 31.1 1.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 1.9 0
vertex 31.1 1.9 0
vertex 31.1 1.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 31.9 1.9 0
vertex 31.1 1.9 4.9
vertex 31.9 1.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 1.9 0
vertex 31.1 1.1 0
vertex 31.1 1.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 31.1 1.9 0
vertex 31.1 1.1 4.9
vertex 31.1 1.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 1.1 0
vertex 31.9 1.9 0
vertex 31.9 1.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 31.9 1.1 0
vertex 31.9 1.9 4.9
vertex 31.9 1.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 6.1 4.9
vertex 32.9 6.1 4.9
vertex 32.9 6.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 6.1 4.9
vertex 32.9 6.9 4.9
vertex 32.1 6.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 6.1 0
vertex 32.9 6.1 0
vertex 32.9 6.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 6.1 0
vertex 32.9 6.1 4.9
vertex 32.1 6.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 6.9 0
vertex 32.1 6.9 0
vertex 32.1 6.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 6.9 0
vertex 32.1 6.9 4.9
vertex 32.9 6.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 6.9 0
vertex 32.1 6.1 0
vertex 32.1 6.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 6.9 0
vertex 32.1 6.1 4.9
vertex 32.1 6.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 6.1 0
vertex 32.9 6.9 0
vertex 32.9 6.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 6.1 0
vertex 32.9 6.9 4.9
vertex 32.9 6.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 4.1 10.55
vertex 32.9 4.1 10.55
vertex 32.9 4.9 10.55
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 4.1 10.55
vertex 32.9 4.9 10.55
vertex 32.1 4.9 10.55
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 4.1 0
vertex 32.9 4.1 0
vertex 32.9 4.1 10.55
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 4.1 0
vertex 32.9 4.1 10.55
vertex 32.1 4.1 10.55
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 4.9 0
vertex 32.1 4.9 0
vertex 32.1 4.9 10.55
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 4.9 0
vertex 32.1 4.9 10.55
vertex 32.9 4.9 10.55
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 4.9 0
vertex 32.1 4.1 0
vertex 32.1 4.1 10.55
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 4.9 0
vertex 32.1 4.1 10.55
vertex 32.1 4.9 10.55
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 4.1 0
vertex 32.9 4.9 0
vertex 32.9 4.9 10.55
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 4.1 0
vertex 32.9 4.9 10.55
vertex 32.9 4.1 10.55
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 3.1 14.79
vertex 32.9 3.1 14.79
vertex 32.9 3.9 14.79
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 3.1 14.79
vertex 32.9 3.9 14.79
vertex 32.1 3.9 14.79
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 3.1 0
vertex 32.9 3.1 0
vertex 32.9 3.1 14.79
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 3.1 0
vertex 32.9 3.1 14.79
vertex 32.1 3.1 14.79
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 3.9 0
vertex 32.1 3.9 0
vertex 32.1 3.9 14.79
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 3.9 0
vertex 32.1 3.9 14.79
vertex 32.9 3.9 14.79
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 3.9 0
vertex 32.1 3.1 0
vertex 32.1 3.1 14.79
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 3.9 0
vertex 32.1 3.1 14.79
vertex 32.1 3.9 14.79
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 3.1 0
vertex 32.9 3.9 0
vertex 32.9 3.9 14.79
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 3.1 0
vertex 32.9 3.9 14.79
vertex 32.9 3.1 14.79
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 2.1 6.09
vertex 32.9 2.1 6.09
vertex 32.9 2.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 2.1 6.09
vertex 32.9 2.9 6.09
vertex 32.1 2.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 2.1 0
vertex 32.9 2.1 0
vertex 32.9 2.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 2.1 0
vertex 32.9 2.1 6.09
vertex 32.1 2.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 2.9 0
vertex 32.1 2.9 0
vertex 32.1 2.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 2.9 0
vertex 32.1 2.9 6.09
vertex 32.9 2.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 2.9 0
vertex 32.1 2.1 0
vertex 32.1 2.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 2.9 0
vertex 32.1 2.1 6.09
vertex 32.1 2.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 2.1 0
vertex 32.9 2.9 0
vertex 32.9 2.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 2.1 0
vertex 32.9 2.9 6.09
vertex 32.9 2.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 1.1 3.16
vertex 32.9 1.1 3.16
vertex 32.9 1.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 1.1 3.16
vertex 32.9 1.9 3.16
vertex 32.1 1.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 1.1 0
vertex 32.9 1.1 0
vertex 32.9 1.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 1.1 0
vertex 32.9 1.1 3.16
vertex 32.1 1.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 1.9 0
vertex 32.1 1.9 0
vertex 32.1 1.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 1.9 0
vertex 32.1 1.9 3.16
vertex 32.9 1.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 1.9 0
vertex 32.1 1.1 0
vertex 32.1 1.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 1.9 0
vertex 32.1 1.1 3.16
vertex 32.1 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 1.1 0
vertex 32.9 1.9 0
vertex 32.9 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 1.1 0
vertex 32.9 1.9 3.16
vertex 32.9 1.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 0.1 12.39
vertex 32.9 0.1 12.39
vertex 32.9 0.9 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 32.1 0.1 12.39
vertex 32.9 0.9 12.39
vertex 32.1 0.9 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 0.1 0
vertex 32.9 0.1 0
vertex 32.9 0.1 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 32.1 0.1 0
vertex 32.9 0.1 12.39
vertex 32.1 0.1 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 0.9 0
vertex 32.1 0.9 0
vertex 32.1 0.9 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 32.9 0.9 0
vertex 32.1 0.9 12.39
vertex 32.9 0.9 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 0.9 0
vertex 32.1 0.1 0
vertex 32.1 0.1 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 32.1 0.9 0
vertex 32.1 0.1 12.39
vertex 32.1 0.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 0.1 0
vertex 32.9 0.9 0
vertex 32.9 0.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 32.9 0.1 0
vertex 32.9 0.9 12.39
vertex 32.9 0.1 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 6.1 10.55
vertex 33.9 6.1 10.55
vertex 33.9 6.9 10.55
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 6.1 10.55
vertex 33.9 6.9 10.55
vertex 33.1 6.9 10.55
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 6.1 0
vertex 33.9 6.1 0
vertex 33.9 6.1 10.55
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 6.1 0
vertex 33.9 6.1 10.55
vertex 33.1 6.1 10.55
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 6.9 0
vertex 33.1 6.9 0
vertex 33.1 6.9 10.55
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 6.9 0
vertex 33.1 6.9 10.55
vertex 33.9 6.9 10.55
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 6.9 0
vertex 33.1 6.1 0
vertex 33.1 6.1 10.55
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 6.9 0
vertex 33.1 6.1 10.55
vertex 33.1 6.9 10.55
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 6.1 0
vertex 33.9 6.9 0
vertex 33.9 6.9 10.55
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 6.1 0
vertex 33.9 6.9 10.55
vertex 33.9 6.1 10.55
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 5.1 3.16
vertex 33.9 5.1 3.16
vertex 33.9 5.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 5.1 3.16
vertex 33.9 5.9 3.16
vertex 33.1 5.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 5.1 0
vertex 33.9 5.1 0
vertex 33.9 5.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 5.1 0
vertex 33.9 5.1 3.16
vertex 33.1 5.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 5.9 0
vertex 33.1 5.9 0
vertex 33.1 5.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 5.9 0
vertex 33.1 5.9 3.16
vertex 33.9 5.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 5.9 0
vertex 33.1 5.1 0
vertex 33.1 5.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 5.9 0
vertex 33.1 5.1 3.16
vertex 33.1 5.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 5.1 0
vertex 33.9 5.9 0
vertex 33.9 5.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 5.1 0
vertex 33.9 5.9 3.16
vertex 33.9 5.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 4.1 4.9
vertex 33.9 4.1 4.9
vertex 33.9 4.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 4.1 4.9
vertex 33.9 4.9 4.9
vertex 33.1 4.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 4.1 0
vertex 33.9 4.1 0
vertex 33.9 4.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 4.1 0
vertex 33.9 4.1 4.9
vertex 33.1 4.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 4.9 0
vertex 33.1 4.9 0
vertex 33.1 4.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 4.9 0
vertex 33.1 4.9 4.9
vertex 33.9 4.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 4.9 0
vertex 33.1 4.1 0
vertex 33.1 4.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 4.9 0
vertex 33.1 4.1 4.9
vertex 33.1 4.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 4.1 0
vertex 33.9 4.9 0
vertex 33.9 4.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 4.1 0
vertex 33.9 4.9 4.9
vertex 33.9 4.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 3.1 3.16
vertex 33.9 3.1 3.16
vertex 33.9 3.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 3.1 3.16
vertex 33.9 3.9 3.16
vertex 33.1 3.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 3.1 0
vertex 33.9 3.1 0
vertex 33.9 3.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 3.1 0
vertex 33.9 3.1 3.16
vertex 33.1 3.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 3.9 0
vertex 33.1 3.9 0
vertex 33.1 3.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 3.9 0
vertex 33.1 3.9 3.16
vertex 33.9 3.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 3.9 0
vertex 33.1 3.1 0
vertex 33.1 3.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 3.9 0
vertex 33.1 3.1 3.16
vertex 33.1 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 3.1 0
vertex 33.9 3.9 0
vertex 33.9 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 3.1 0
vertex 33.9 3.9 3.16
vertex 33.9 3.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 2.1 7.49
vertex 33.9 2.1 7.49
vertex 33.9 2.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 33.1 2.1 7.49
vertex 33.9 2.9 7.49
vertex 33.1 2.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 2.1 0
vertex 33.9 2.1 0
vertex 33.9 2.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 33.1 2.1 0
vertex 33.9 2.1 7.49
vertex 33.1 2.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 2.9 0
vertex 33.1 2.9 0
vertex 33.1 2.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 33.9 2.9 0
vertex 33.1 2.9 7.49
vertex 33.9 2.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 2.9 0
vertex 33.1 2.1 0
vertex 33.1 2.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 33.1 2.9 0
vertex 33.1 2.1 7.49
vertex 33.1 2.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 2.1 0
vertex 33.9 2.9 0
vertex 33.9 2.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 33.9 2.1 0
vertex 33.9 2.9 7.49
vertex 33.9 2.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 34.1 3.1 5.53
vertex 34.9 3.1 5.53
vertex 34.9 3.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 34.1 3.1 5.53
vertex 34.9 3.9 5.53
vertex 34.1 3.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 34.1 3.1 0
vertex 34.9 3.1 0
vertex 34.9 3.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 34.1 3.1 0
vertex 34.9 3.1 5.53
vertex 34.1 3.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 34.9 3.9 0
vertex 34.1 3.9 0
vertex 34.1 3.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 34.9 3.9 0
vertex 34.1 3.9 5.53
vertex 34.9 3.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 34.1 3.9 0
vertex 34.1 3.1 0
vertex 34.1 3.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 34.1 3.9 0
vertex 34.1 3.1 5.53
vertex 34.1 3.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 34.9 3.1 0
vertex 34.9 3.9 0
vertex 34.9 3.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 34.9 3.1 0
vertex 34.9 3.9 5.53
vertex 34.9 3.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 35.1 5.1 7.89
vertex 35.9 5.1 7.89
vertex 35.9 5.9 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 35.1 5.1 7.89
vertex 35.9 5.9 7.89
vertex 35.1 5.9 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.1 5.1 0
vertex 35.9 5.1 0
vertex 35.9 5.1 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.1 5.1 0
vertex 35.9 5.1 7.89
vertex 35.1 5.1 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.9 5.9 0
vertex 35.1 5.9 0
vertex 35.1 5.9 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.9 5.9 0
vertex 35.1 5.9 7.89
vertex 35.9 5.9 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 35.1 5.9 0
vertex 35.1 5.1 0
vertex 35.1 5.1 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 35.1 5.9 0
vertex 35.1 5.1 7.89
vertex 35.1 5.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 35.9 5.1 0
vertex 35.9 5.9 0
vertex 35.9 5.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 35.9 5.1 0
vertex 35.9 5.9 7.89
vertex 35.9 5.1 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 35.1 4.1 7.89
vertex 35.9 4.1 7.89
vertex 35.9 4.9 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 35.1 4.1 7.89
vertex 35.9 4.9 7.89
vertex 35.1 4.9 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.1 4.1 0
vertex 35.9 4.1 0
vertex 35.9 4.1 7.89
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.1 4.1 0
vertex 35.9 4.1 7.89
vertex 35.1 4.1 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.9 4.9 0
vertex 35.1 4.9 0
vertex 35.1 4.9 7.89
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.9 4.9 0
vertex 35.1 4.9 7.89
vertex 35.9 4.9 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 35.1 4.9 0
vertex 35.1 4.1 0
vertex 35.1 4.1 7.89
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 35.1 4.9 0
vertex 35.1 4.1 7.89
vertex 35.1 4.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 35.9 4.1 0
vertex 35.9 4.9 0
vertex 35.9 4.9 7.89
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 35.9 4.1 0
vertex 35.9 4.9 7.89
vertex 35.9 4.1 7.89
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 35.1 3.1 9.96
vertex 35.9 3.1 9.96
vertex 35.9 3.9 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 35.1 3.1 9.96
vertex 35.9 3.9 9.96
vertex 35.1 3.9 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.1 3.1 0
vertex 35.9 3.1 0
vertex 35.9 3.1 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.1 3.1 0
vertex 35.9 3.1 9.96
vertex 35.1 3.1 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.9 3.9 0
vertex 35.1 3.9 0
vertex 35.1 3.9 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.9 3.9 0
vertex 35.1 3.9 9.96
vertex 35.9 3.9 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 35.1 3.9 0
vertex 35.1 3.1 0
vertex 35.1 3.1 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 35.1 3.9 0
vertex 35.1 3.1 9.96
vertex 35.1 3.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 35.9 3.1 0
vertex 35.9 3.9 0
vertex 35.9 3.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 35.9 3.1 0
vertex 35.9 3.9 9.96
vertex 35.9 3.1 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 35.1 1.1 6.59
vertex 35.9 1.1 6.59
vertex 35.9 1.9 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 35.1 1.1 6.59
vertex 35.9 1.9 6.59
vertex 35.1 1.9 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.1 1.1 0
vertex 35.9 1.1 0
vertex 35.9 1.1 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 35.1 1.1 0
vertex 35.9 1.1 6.59
vertex 35.1 1.1 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.9 1.9 0
vertex 35.1 1.9 0
vertex 35.1 1.9 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 35.9 1.9 0
vertex 35.1 1.9 6.59
vertex 35.9 1.9 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 35.1 1.9 0
vertex 35.1 1.1 0
vertex 35.1 1.1 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 35.1 1.9 0
vertex 35.1 1.1 6.59
vertex 35.1 1.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 35.9 1.1 0
vertex 35.9 1.9 0
vertex 35.9 1.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 35.9 1.1 0
vertex 35.9 1.9 6.59
vertex 35.9 1.1 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 36.1 6.1 4.14
vertex 36.9 6.1 4.14
vertex 36.9 6.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 36.1 6.1 4.14
vertex 36.9 6.9 4.14
vertex 36.1 6.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 36.1 6.1 0
vertex 36.9 6.1 0
vertex 36.9 6.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 36.1 6.1 0
vertex 36.9 6.1 4.14
vertex 36.1 6.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 36.9 6.9 0
vertex 36.1 6.9 0
vertex 36.1 6.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 36.9 6.9 0
vertex 36.1 6.9 4.14
vertex 36.9 6.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 36.1 6.9 0
vertex 36.1 6.1 0
vertex 36.1 6.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 36.1 6.9 0
vertex 36.1 6.1 4.14
vertex 36.1 6.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 36.9 6.1 0
vertex 36.9 6.9 0
vertex 36.9 6.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 36.9 6.1 0
vertex 36.9 6.9 4.14
vertex 36.9 6.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 36.1 5.1 7.06
vertex 36.9 5.1 7.06
vertex 36.9 5.9 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 36.1 5.1 7.06
vertex 36.9 5.9 7.06
vertex 36.1 5.9 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 36.1 5.1 0
vertex 36.9 5.1 0
vertex 36.9 5.1 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 36.1 5.1 0
vertex 36.9 5.1 7.06
vertex 36.1 5.1 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 36.9 5.9 0
vertex 36.1 5.9 0
vertex 36.1 5.9 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 36.9 5.9 0
vertex 36.1 5.9 7.06
vertex 36.9 5.9 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 36.1 5.9 0
vertex 36.1 5.1 0
vertex 36.1 5.1 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 36.1 5.9 0
vertex 36.1 5.1 7.06
vertex 36.1 5.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 36.9 5.1 0
vertex 36.9 5.9 0
vertex 36.9 5.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 36.9 5.1 0
vertex 36.9 5.9 7.06
vertex 36.9 5.1 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 36.1 4.1 6.59
vertex 36.9 4.1 6.59
vertex 36.9 4.9 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 36.1 4.1 6.59
vertex 36.9 4.9 6.59
vertex 36.1 4.9 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 36.1 4.1 0
vertex 36.9 4.1 0
vertex 36.9 4.1 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 36.1 4.1 0
vertex 36.9 4.1 6.59
vertex 36.1 4.1 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 36.9 4.9 0
vertex 36.1 4.9 0
vertex 36.1 4.9 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 36.9 4.9 0
vertex 36.1 4.9 6.59
vertex 36.9 4.9 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 36.1 4.9 0
vertex 36.1 4.1 0
vertex 36.1 4.1 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 36.1 4.9 0
vertex 36.1 4.1 6.59
vertex 36.1 4.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 36.9 4.1 0
vertex 36.9 4.9 0
vertex 36.9 4.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 36.9 4.1 0
vertex 36.9 4.9 6.59
vertex 36.9 4.1 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 36.1 1.1 4.14
vertex 36.9 1.1 4.14
vertex 36.9 1.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 36.1 1.1 4.14
vertex 36.9 1.9 4.14
vertex 36.1 1.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 36.1 1.1 0
vertex 36.9 1.1 0
vertex 36.9 1.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 36.1 1.1 0
vertex 36.9 1.1 4.14
vertex 36.1 1.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 36.9 1.9 0
vertex 36.1 1.9 0
vertex 36.1 1.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 36.9 1.9 0
vertex 36.1 1.9 4.14
vertex 36.9 1.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 36.1 1.9 0
vertex 36.1 1.1 0
vertex 36.1 1.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 36.1 1.9 0
vertex 36.1 1.1 4.14
vertex 36.1 1.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 36.9 1.1 0
vertex 36.9 1.9 0
vertex 36.9 1.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 36.9 1.1 0
vertex 36.9 1.9 4.14
vertex 36.9 1.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 6.1 4.14
vertex 37.9 6.1 4.14
vertex 37.9 6.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 6.1 4.14
vertex 37.9 6.9 4.14
vertex 37.1 6.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 6.1 0
vertex 37.9 6.1 0
vertex 37.9 6.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 6.1 0
vertex 37.9 6.1 4.14
vertex 37.1 6.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 6.9 0
vertex 37.1 6.9 0
vertex 37.1 6.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 6.9 0
vertex 37.1 6.9 4.14
vertex 37.9 6.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 6.9 0
vertex 37.1 6.1 0
vertex 37.1 6.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 6.9 0
vertex 37.1 6.1 4.14
vertex 37.1 6.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 6.1 0
vertex 37.9 6.9 0
vertex 37.9 6.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 6.1 0
vertex 37.9 6.9 4.14
vertex 37.9 6.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 4.1 4.14
vertex 37.9 4.1 4.14
vertex 37.9 4.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 4.1 4.14
vertex 37.9 4.9 4.14
vertex 37.1 4.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 4.1 0
vertex 37.9 4.1 0
vertex 37.9 4.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 4.1 0
vertex 37.9 4.1 4.14
vertex 37.1 4.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 4.9 0
vertex 37.1 4.9 0
vertex 37.1 4.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 4.9 0
vertex 37.1 4.9 4.14
vertex 37.9 4.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 4.9 0
vertex 37.1 4.1 0
vertex 37.1 4.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 4.9 0
vertex 37.1 4.1 4.14
vertex 37.1 4.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 4.1 0
vertex 37.9 4.9 0
vertex 37.9 4.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 4.1 0
vertex 37.9 4.9 4.14
vertex 37.9 4.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 3.1 4.14
vertex 37.9 3.1 4.14
vertex 37.9 3.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 3.1 4.14
vertex 37.9 3.9 4.14
vertex 37.1 3.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 3.1 0
vertex 37.9 3.1 0
vertex 37.9 3.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 3.1 0
vertex 37.9 3.1 4.14
vertex 37.1 3.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 3.9 0
vertex 37.1 3.9 0
vertex 37.1 3.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 3.9 0
vertex 37.1 3.9 4.14
vertex 37.9 3.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 3.9 0
vertex 37.1 3.1 0
vertex 37.1 3.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 3.9 0
vertex 37.1 3.1 4.14
vertex 37.1 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 3.1 0
vertex 37.9 3.9 0
vertex 37.9 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 3.1 0
vertex 37.9 3.9 4.14
vertex 37.9 3.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 2.1 8.64
vertex 37.9 2.1 8.64
vertex 37.9 2.9 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 2.1 8.64
vertex 37.9 2.9 8.64
vertex 37.1 2.9 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 2.1 0
vertex 37.9 2.1 0
vertex 37.9 2.1 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 2.1 0
vertex 37.9 2.1 8.64
vertex 37.1 2.1 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 2.9 0
vertex 37.1 2.9 0
vertex 37.1 2.9 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 2.9 0
vertex 37.1 2.9 8.64
vertex 37.9 2.9 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 2.9 0
vertex 37.1 2.1 0
vertex 37.1 2.1 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 2.9 0
vertex 37.1 2.1 8.64
vertex 37.1 2.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 2.1 0
vertex 37.9 2.9 0
vertex 37.9 2.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 2.1 0
vertex 37.9 2.9 8.64
vertex 37.9 2.1 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 1.1 3.16
vertex 37.9 1.1 3.16
vertex 37.9 1.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 1.1 3.16
vertex 37.9 1.9 3.16
vertex 37.1 1.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 1.1 0
vertex 37.9 1.1 0
vertex 37.9 1.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 1.1 0
vertex 37.9 1.1 3.16
vertex 37.1 1.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 1.9 0
vertex 37.1 1.9 0
vertex 37.1 1.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 1.9 0
vertex 37.1 1.9 3.16
vertex 37.9 1.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 1.9 0
vertex 37.1 1.1 0
vertex 37.1 1.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 1.9 0
vertex 37.1 1.1 3.16
vertex 37.1 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 1.1 0
vertex 37.9 1.9 0
vertex 37.9 1.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 1.1 0
vertex 37.9 1.9 3.16
vertex 37.9 1.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 0.1 3.16
vertex 37.9 0.1 3.16
vertex 37.9 0.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 37.1 0.1 3.16
vertex 37.9 0.9 3.16
vertex 37.1 0.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 0.1 0
vertex 37.9 0.1 0
vertex 37.9 0.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 37.1 0.1 0
vertex 37.9 0.1 3.16
vertex 37.1 0.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 0.9 0
vertex 37.1 0.9 0
vertex 37.1 0.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 37.9 0.9 0
vertex 37.1 0.9 3.16
vertex 37.9 0.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 0.9 0
vertex 37.1 0.1 0
vertex 37.1 0.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 37.1 0.9 0
vertex 37.1 0.1 3.16
vertex 37.1 0.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 0.1 0
vertex 37.9 0.9 0
vertex 37.9 0.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 37.9 0.1 0
vertex 37.9 0.9 3.16
vertex 37.9 0.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 6.1 6.09
vertex 38.9 6.1 6.09
vertex 38.9 6.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 6.1 6.09
vertex 38.9 6.9 6.09
vertex 38.1 6.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 6.1 0
vertex 38.9 6.1 0
vertex 38.9 6.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 6.1 0
vertex 38.9 6.1 6.09
vertex 38.1 6.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 6.9 0
vertex 38.1 6.9 0
vertex 38.1 6.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 6.9 0
vertex 38.1 6.9 6.09
vertex 38.9 6.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 6.9 0
vertex 38.1 6.1 0
vertex 38.1 6.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 6.9 0
vertex 38.1 6.1 6.09
vertex 38.1 6.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 6.1 0
vertex 38.9 6.9 0
vertex 38.9 6.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 6.1 0
vertex 38.9 6.9 6.09
vertex 38.9 6.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 5.1 6.09
vertex 38.9 5.1 6.09
vertex 38.9 5.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 5.1 6.09
vertex 38.9 5.9 6.09
vertex 38.1 5.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 5.1 0
vertex 38.9 5.1 0
vertex 38.9 5.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 5.1 0
vertex 38.9 5.1 6.09
vertex 38.1 5.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 5.9 0
vertex 38.1 5.9 0
vertex 38.1 5.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 5.9 0
vertex 38.1 5.9 6.09
vertex 38.9 5.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 5.9 0
vertex 38.1 5.1 0
vertex 38.1 5.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 5.9 0
vertex 38.1 5.1 6.09
vertex 38.1 5.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 5.1 0
vertex 38.9 5.9 0
vertex 38.9 5.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 5.1 0
vertex 38.9 5.9 6.09
vertex 38.9 5.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 4.1 9.65
vertex 38.9 4.1 9.65
vertex 38.9 4.9 9.65
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 4.1 9.65
vertex 38.9 4.9 9.65
vertex 38.1 4.9 9.65
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 4.1 0
vertex 38.9 4.1 0
vertex 38.9 4.1 9.65
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 4.1 0
vertex 38.9 4.1 9.65
vertex 38.1 4.1 9.65
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 4.9 0
vertex 38.1 4.9 0
vertex 38.1 4.9 9.65
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 4.9 0
vertex 38.1 4.9 9.65
vertex 38.9 4.9 9.65
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 4.9 0
vertex 38.1 4.1 0
vertex 38.1 4.1 9.65
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 4.9 0
vertex 38.1 4.1 9.65
vertex 38.1 4.9 9.65
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 4.1 0
vertex 38.9 4.9 0
vertex 38.9 4.9 9.65
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 4.1 0
vertex 38.9 4.9 9.65
vertex 38.9 4.1 9.65
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 2.1 11.11
vertex 38.9 2.1 11.11
vertex 38.9 2.9 11.11
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 2.1 11.11
vertex 38.9 2.9 11.11
vertex 38.1 2.9 11.11
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 2.1 0
vertex 38.9 2.1 0
vertex 38.9 2.1 11.11
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 2.1 0
vertex 38.9 2.1 11.11
vertex 38.1 2.1 11.11
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 2.9 0
vertex 38.1 2.9 0
vertex 38.1 2.9 11.11
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 2.9 0
vertex 38.1 2.9 11.11
vertex 38.9 2.9 11.11
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 2.9 0
vertex 38.1 2.1 0
vertex 38.1 2.1 11.11
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 2.9 0
vertex 38.1 2.1 11.11
vertex 38.1 2.9 11.11
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 2.1 0
vertex 38.9 2.9 0
vertex 38.9 2.9 11.11
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 2.1 0
vertex 38.9 2.9 11.11
vertex 38.9 2.1 11.11
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 1.1 7.49
vertex 38.9 1.1 7.49
vertex 38.9 1.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 1.1 7.49
vertex 38.9 1.9 7.49
vertex 38.1 1.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 1.1 0
vertex 38.9 1.1 0
vertex 38.9 1.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 1.1 0
vertex 38.9 1.1 7.49
vertex 38.1 1.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 1.9 0
vertex 38.1 1.9 0
vertex 38.1 1.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 1.9 0
vertex 38.1 1.9 7.49
vertex 38.9 1.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 1.9 0
vertex 38.1 1.1 0
vertex 38.1 1.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 1.9 0
vertex 38.1 1.1 7.49
vertex 38.1 1.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 1.1 0
vertex 38.9 1.9 0
vertex 38.9 1.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 1.1 0
vertex 38.9 1.9 7.49
vertex 38.9 1.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 0.1 4.14
vertex 38.9 0.1 4.14
vertex 38.9 0.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 38.1 0.1 4.14
vertex 38.9 0.9 4.14
vertex 38.1 0.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 0.1 0
vertex 38.9 0.1 0
vertex 38.9 0.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 38.1 0.1 0
vertex 38.9 0.1 4.14
vertex 38.1 0.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 0.9 0
vertex 38.1 0.9 0
vertex 38.1 0.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 38.9 0.9 0
vertex 38.1 0.9 4.14
vertex 38.9 0.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 0.9 0
vertex 38.1 0.1 0
vertex 38.1 0.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 38.1 0.9 0
vertex 38.1 0.1 4.14
vertex 38.1 0.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 0.1 0
vertex 38.9 0.9 0
vertex 38.9 0.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 38.9 0.1 0
vertex 38.9 0.9 4.14
vertex 38.9 0.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 39.1 6.1 4.9
vertex 39.9 6.1 4.9
vertex 39.9 6.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 39.1 6.1 4.9
vertex 39.9 6.9 4.9
vertex 39.1 6.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 39.1 6.1 0
vertex 39.9 6.1 0
vertex 39.9 6.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 39.1 6.1 0
vertex 39.9 6.1 4.9
vertex 39.1 6.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 39.9 6.9 0
vertex 39.1 6.9 0
vertex 39.1 6.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 39.9 6.9 0
vertex 39.1 6.9 4.9
vertex 39.9 6.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 39.1 6.9 0
vertex 39.1 6.1 0
vertex 39.1 6.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 39.1 6.9 0
vertex 39.1 6.1 4.9
vertex 39.1 6.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 39.9 6.1 0
vertex 39.9 6.9 0
vertex 39.9 6.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 39.9 6.1 0
vertex 39.9 6.9 4.9
vertex 39.9 6.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 39.1 5.1 10.26
vertex 39.9 5.1 10.26
vertex 39.9 5.9 10.26
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 39.1 5.1 10.26
vertex 39.9 5.9 10.26
vertex 39.1 5.9 10.26
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 39.1 5.1 0
vertex 39.9 5.1 0
vertex 39.9 5.1 10.26
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 39.1 5.1 0
vertex 39.9 5.1 10.26
vertex 39.1 5.1 10.26
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 39.9 5.9 0
vertex 39.1 5.9 0
vertex 39.1 5.9 10.26
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 39.9 5.9 0
vertex 39.1 5.9 10.26
vertex 39.9 5.9 10.26
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 39.1 5.9 0
vertex 39.1 5.1 0
vertex 39.1 5.1 10.26
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 39.1 5.9 0
vertex 39.1 5.1 10.26
vertex 39.1 5.9 10.26
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 39.9 5.1 0
vertex 39.9 5.9 0
vertex 39.9 5.9 10.26
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 39.9 5.1 0
vertex 39.9 5.9 10.26
vertex 39.9 5.1 10.26
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 39.1 4.1 9.33
vertex 39.9 4.1 9.33
vertex 39.9 4.9 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 39.1 4.1 9.33
vertex 39.9 4.9 9.33
vertex 39.1 4.9 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 39.1 4.1 0
vertex 39.9 4.1 0
vertex 39.9 4.1 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 39.1 4.1 0
vertex 39.9 4.1 9.33
vertex 39.1 4.1 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 39.9 4.9 0
vertex 39.1 4.9 0
vertex 39.1 4.9 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 39.9 4.9 0
vertex 39.1 4.9 9.33
vertex 39.9 4.9 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 39.1 4.9 0
vertex 39.1 4.1 0
vertex 39.1 4.1 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 39.1 4.9 0
vertex 39.1 4.1 9.33
vertex 39.1 4.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 39.9 4.1 0
vertex 39.9 4.9 0
vertex 39.9 4.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 39.9 4.1 0
vertex 39.9 4.9 9.33
vertex 39.9 4.1 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 39.1 3.1 4.14
vertex 39.9 3.1 4.14
vertex 39.9 3.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 39.1 3.1 4.14
vertex 39.9 3.9 4.14
vertex 39.1 3.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 39.1 3.1 0
vertex 39.9 3.1 0
vertex 39.9 3.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 39.1 3.1 0
vertex 39.9 3.1 4.14
vertex 39.1 3.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 39.9 3.9 0
vertex 39.1 3.9 0
vertex 39.1 3.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 39.9 3.9 0
vertex 39.1 3.9 4.14
vertex 39.9 3.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 39.1 3.9 0
vertex 39.1 3.1 0
vertex 39.1 3.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 39.1 3.9 0
vertex 39.1 3.1 4.14
vertex 39.1 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 39.9 3.1 0
vertex 39.9 3.9 0
vertex 39.9 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 39.9 3.1 0
vertex 39.9 3.9 4.14
vertex 39.9 3.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 40.1 6.1 3.16
vertex 40.9 6.1 3.16
vertex 40.9 6.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 40.1 6.1 3.16
vertex 40.9 6.9 3.16
vertex 40.1 6.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 40.1 6.1 0
vertex 40.9 6.1 0
vertex 40.9 6.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 40.1 6.1 0
vertex 40.9 6.1 3.16
vertex 40.1 6.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 40.9 6.9 0
vertex 40.1 6.9 0
vertex 40.1 6.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 40.9 6.9 0
vertex 40.1 6.9 3.16
vertex 40.9 6.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 40.1 6.9 0
vertex 40.1 6.1 0
vertex 40.1 6.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 40.1 6.9 0
vertex 40.1 6.1 3.16
vertex 40.1 6.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 40.9 6.1 0
vertex 40.9 6.9 0
vertex 40.9 6.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 40.9 6.1 0
vertex 40.9 6.9 3.16
vertex 40.9 6.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 41.1 4.1 6.09
vertex 41.9 4.1 6.09
vertex 41.9 4.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 41.1 4.1 6.09
vertex 41.9 4.9 6.09
vertex 41.1 4.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 41.1 4.1 0
vertex 41.9 4.1 0
vertex 41.9 4.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 41.1 4.1 0
vertex 41.9 4.1 6.09
vertex 41.1 4.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 41.9 4.9 0
vertex 41.1 4.9 0
vertex 41.1 4.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 41.9 4.9 0
vertex 41.1 4.9 6.09
vertex 41.9 4.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 41.1 4.9 0
vertex 41.1 4.1 0
vertex 41.1 4.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 41.1 4.9 0
vertex 41.1 4.1 6.09
vertex 41.1 4.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 41.9 4.1 0
vertex 41.9 4.9 0
vertex 41.9 4.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 41.9 4.1 0
vertex 41.9 4.9 6.09
vertex 41.9 4.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 41.1 3.1 3.16
vertex 41.9 3.1 3.16
vertex 41.9 3.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 41.1 3.1 3.16
vertex 41.9 3.9 3.16
vertex 41.1 3.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 41.1 3.1 0
vertex 41.9 3.1 0
vertex 41.9 3.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 41.1 3.1 0
vertex 41.9 3.1 3.16
vertex 41.1 3.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 41.9 3.9 0
vertex 41.1 3.9 0
vertex 41.1 3.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 41.9 3.9 0
vertex 41.1 3.9 3.16
vertex 41.9 3.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 41.1 3.9 0
vertex 41.1 3.1 0
vertex 41.1 3.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 41.1 3.9 0
vertex 41.1 3.1 3.16
vertex 41.1 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 41.9 3.1 0
vertex 41.9 3.9 0
vertex 41.9 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 41.9 3.1 0
vertex 41.9 3.9 3.16
vertex 41.9 3.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 42.1 5.1 6.59
vertex 42.9 5.1 6.59
vertex 42.9 5.9 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 42.1 5.1 6.59
vertex 42.9 5.9 6.59
vertex 42.1 5.9 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 42.1 5.1 0
vertex 42.9 5.1 0
vertex 42.9 5.1 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 42.1 5.1 0
vertex 42.9 5.1 6.59
vertex 42.1 5.1 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 42.9 5.9 0
vertex 42.1 5.9 0
vertex 42.1 5.9 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 42.9 5.9 0
vertex 42.1 5.9 6.59
vertex 42.9 5.9 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 42.1 5.9 0
vertex 42.1 5.1 0
vertex 42.1 5.1 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 42.1 5.9 0
vertex 42.1 5.1 6.59
vertex 42.1 5.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 42.9 5.1 0
vertex 42.9 5.9 0
vertex 42.9 5.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 42.9 5.1 0
vertex 42.9 5.9 6.59
vertex 42.9 5.1 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 42.1 4.1 7.06
vertex 42.9 4.1 7.06
vertex 42.9 4.9 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 42.1 4.1 7.06
vertex 42.9 4.9 7.06
vertex 42.1 4.9 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 42.1 4.1 0
vertex 42.9 4.1 0
vertex 42.9 4.1 7.06
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 42.1 4.1 0
vertex 42.9 4.1 7.06
vertex 42.1 4.1 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 42.9 4.9 0
vertex 42.1 4.9 0
vertex 42.1 4.9 7.06
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 42.9 4.9 0
vertex 42.1 4.9 7.06
vertex 42.9 4.9 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 42.1 4.9 0
vertex 42.1 4.1 0
vertex 42.1 4.1 7.06
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 42.1 4.9 0
vertex 42.1 4.1 7.06
vertex 42.1 4.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 42.9 4.1 0
vertex 42.9 4.9 0
vertex 42.9 4.9 7.06
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 42.9 4.1 0
vertex 42.9 4.9 7.06
vertex 42.9 4.1 7.06
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 5.1 4.9
vertex 43.9 5.1 4.9
vertex 43.9 5.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 5.1 4.9
vertex 43.9 5.9 4.9
vertex 43.1 5.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 5.1 0
vertex 43.9 5.1 0
vertex 43.9 5.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 5.1 0
vertex 43.9 5.1 4.9
vertex 43.1 5.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 5.9 0
vertex 43.1 5.9 0
vertex 43.1 5.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 5.9 0
vertex 43.1 5.9 4.9
vertex 43.9 5.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 5.9 0
vertex 43.1 5.1 0
vertex 43.1 5.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 5.9 0
vertex 43.1 5.1 4.9
vertex 43.1 5.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 5.1 0
vertex 43.9 5.9 0
vertex 43.9 5.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 5.1 0
vertex 43.9 5.9 4.9
vertex 43.9 5.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 4.1 4.14
vertex 43.9 4.1 4.14
vertex 43.9 4.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 4.1 4.14
vertex 43.9 4.9 4.14
vertex 43.1 4.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 4.1 0
vertex 43.9 4.1 0
vertex 43.9 4.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 4.1 0
vertex 43.9 4.1 4.14
vertex 43.1 4.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 4.9 0
vertex 43.1 4.9 0
vertex 43.1 4.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 4.9 0
vertex 43.1 4.9 4.14
vertex 43.9 4.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 4.9 0
vertex 43.1 4.1 0
vertex 43.1 4.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 4.9 0
vertex 43.1 4.1 4.14
vertex 43.1 4.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 4.1 0
vertex 43.9 4.9 0
vertex 43.9 4.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 4.1 0
vertex 43.9 4.9 4.14
vertex 43.9 4.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 3.1 8.64
vertex 43.9 3.1 8.64
vertex 43.9 3.9 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 3.1 8.64
vertex 43.9 3.9 8.64
vertex 43.1 3.9 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 3.1 0
vertex 43.9 3.1 0
vertex 43.9 3.1 8.64
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 3.1 0
vertex 43.9 3.1 8.64
vertex 43.1 3.1 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 3.9 0
vertex 43.1 3.9 0
vertex 43.1 3.9 8.64
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 3.9 0
vertex 43.1 3.9 8.64
vertex 43.9 3.9 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 3.9 0
vertex 43.1 3.1 0
vertex 43.1 3.1 8.64
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 3.9 0
vertex 43.1 3.1 8.64
vertex 43.1 3.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 3.1 0
vertex 43.9 3.9 0
vertex 43.9 3.9 8.64
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 3.1 0
vertex 43.9 3.9 8.64
vertex 43.9 3.1 8.64
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 2.1 3.16
vertex 43.9 2.1 3.16
vertex 43.9 2.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 2.1 3.16
vertex 43.9 2.9 3.16
vertex 43.1 2.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 2.1 0
vertex 43.9 2.1 0
vertex 43.9 2.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 2.1 0
vertex 43.9 2.1 3.16
vertex 43.1 2.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 2.9 0
vertex 43.1 2.9 0
vertex 43.1 2.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 2.9 0
vertex 43.1 2.9 3.16
vertex 43.9 2.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 2.9 0
vertex 43.1 2.1 0
vertex 43.1 2.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 2.9 0
vertex 43.1 2.1 3.16
vertex 43.1 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 2.1 0
vertex 43.9 2.9 0
vertex 43.9 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 2.1 0
vertex 43.9 2.9 3.16
vertex 43.9 2.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 1.1 4.14
vertex 43.9 1.1 4.14
vertex 43.9 1.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 1.1 4.14
vertex 43.9 1.9 4.14
vertex 43.1 1.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 1.1 0
vertex 43.9 1.1 0
vertex 43.9 1.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 1.1 0
vertex 43.9 1.1 4.14
vertex 43.1 1.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 1.9 0
vertex 43.1 1.9 0
vertex 43.1 1.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 1.9 0
vertex 43.1 1.9 4.14
vertex 43.9 1.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 1.9 0
vertex 43.1 1.1 0
vertex 43.1 1.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 1.9 0
vertex 43.1 1.1 4.14
vertex 43.1 1.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 1.1 0
vertex 43.9 1.9 0
vertex 43.9 1.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 1.1 0
vertex 43.9 1.9 4.14
vertex 43.9 1.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 0.1 13.09
vertex 43.9 0.1 13.09
vertex 43.9 0.9 13.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 43.1 0.1 13.09
vertex 43.9 0.9 13.09
vertex 43.1 0.9 13.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 0.1 0
vertex 43.9 0.1 0
vertex 43.9 0.1 13.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 43.1 0.1 0
vertex 43.9 0.1 13.09
vertex 43.1 0.1 13.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 0.9 0
vertex 43.1 0.9 0
vertex 43.1 0.9 13.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 43.9 0.9 0
vertex 43.1 0.9 13.09
vertex 43.9 0.9 13.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 0.9 0
vertex 43.1 0.1 0
vertex 43.1 0.1 13.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 43.1 0.9 0
vertex 43.1 0.1 13.09
vertex 43.1 0.9 13.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 0.1 0
vertex 43.9 0.9 0
vertex 43.9 0.9 13.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 43.9 0.1 0
vertex 43.9 0.9 13.09
vertex 43.9 0.1 13.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 6.1 10.55
vertex 44.9 6.1 10.55
vertex 44.9 6.9 10.55
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 6.1 10.55
vertex 44.9 6.9 10.55
vertex 44.1 6.9 10.55
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 6.1 0
vertex 44.9 6.1 0
vertex 44.9 6.1 10.55
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 6.1 0
vertex 44.9 6.1 10.55
vertex 44.1 6.1 10.55
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 6.9 0
vertex 44.1 6.9 0
vertex 44.1 6.9 10.55
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 6.9 0
vertex 44.1 6.9 10.55
vertex 44.9 6.9 10.55
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 6.9 0
vertex 44.1 6.1 0
vertex 44.1 6.1 10.55
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 6.9 0
vertex 44.1 6.1 10.55
vertex 44.1 6.9 10.55
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 6.1 0
vertex 44.9 6.9 0
vertex 44.9 6.9 10.55
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 6.1 0
vertex 44.9 6.9 10.55
vertex 44.9 6.1 10.55
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 5.1 11.11
vertex 44.9 5.1 11.11
vertex 44.9 5.9 11.11
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 5.1 11.11
vertex 44.9 5.9 11.11
vertex 44.1 5.9 11.11
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 5.1 0
vertex 44.9 5.1 0
vertex 44.9 5.1 11.11
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 5.1 0
vertex 44.9 5.1 11.11
vertex 44.1 5.1 11.11
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 5.9 0
vertex 44.1 5.9 0
vertex 44.1 5.9 11.11
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 5.9 0
vertex 44.1 5.9 11.11
vertex 44.9 5.9 11.11
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 5.9 0
vertex 44.1 5.1 0
vertex 44.1 5.1 11.11
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 5.9 0
vertex 44.1 5.1 11.11
vertex 44.1 5.9 11.11
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 5.1 0
vertex 44.9 5.9 0
vertex 44.9 5.9 11.11
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 5.1 0
vertex 44.9 5.9 11.11
vertex 44.9 5.1 11.11
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 3.1 6.59
vertex 44.9 3.1 6.59
vertex 44.9 3.9 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 3.1 6.59
vertex 44.9 3.9 6.59
vertex 44.1 3.9 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 3.1 0
vertex 44.9 3.1 0
vertex 44.9 3.1 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 3.1 0
vertex 44.9 3.1 6.59
vertex 44.1 3.1 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 3.9 0
vertex 44.1 3.9 0
vertex 44.1 3.9 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 3.9 0
vertex 44.1 3.9 6.59
vertex 44.9 3.9 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 3.9 0
vertex 44.1 3.1 0
vertex 44.1 3.1 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 3.9 0
vertex 44.1 3.1 6.59
vertex 44.1 3.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 3.1 0
vertex 44.9 3.9 0
vertex 44.9 3.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 3.1 0
vertex 44.9 3.9 6.59
vertex 44.9 3.1 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 2.1 3.16
vertex 44.9 2.1 3.16
vertex 44.9 2.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 2.1 3.16
vertex 44.9 2.9 3.16
vertex 44.1 2.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 2.1 0
vertex 44.9 2.1 0
vertex 44.9 2.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 2.1 0
vertex 44.9 2.1 3.16
vertex 44.1 2.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 2.9 0
vertex 44.1 2.9 0
vertex 44.1 2.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 2.9 0
vertex 44.1 2.9 3.16
vertex 44.9 2.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 2.9 0
vertex 44.1 2.1 0
vertex 44.1 2.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 2.9 0
vertex 44.1 2.1 3.16
vertex 44.1 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 2.1 0
vertex 44.9 2.9 0
vertex 44.9 2.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 2.1 0
vertex 44.9 2.9 3.16
vertex 44.9 2.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 1.1 5.53
vertex 44.9 1.1 5.53
vertex 44.9 1.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 44.1 1.1 5.53
vertex 44.9 1.9 5.53
vertex 44.1 1.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 1.1 0
vertex 44.9 1.1 0
vertex 44.9 1.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 44.1 1.1 0
vertex 44.9 1.1 5.53
vertex 44.1 1.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 1.9 0
vertex 44.1 1.9 0
vertex 44.1 1.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 44.9 1.9 0
vertex 44.1 1.9 5.53
vertex 44.9 1.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 1.9 0
vertex 44.1 1.1 0
vertex 44.1 1.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 44.1 1.9 0
vertex 44.1 1.1 5.53
vertex 44.1 1.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 1.1 0
vertex 44.9 1.9 0
vertex 44.9 1.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 44.9 1.1 0
vertex 44.9 1.9 5.53
vertex 44.9 1.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 45.1 6.1 4.14
vertex 45.9 6.1 4.14
vertex 45.9 6.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 45.1 6.1 4.14
vertex 45.9 6.9 4.14
vertex 45.1 6.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 45.1 6.1 0
vertex 45.9 6.1 0
vertex 45.9 6.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 45.1 6.1 0
vertex 45.9 6.1 4.14
vertex 45.1 6.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 45.9 6.9 0
vertex 45.1 6.9 0
vertex 45.1 6.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 45.9 6.9 0
vertex 45.1 6.9 4.14
vertex 45.9 6.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 45.1 6.9 0
vertex 45.1 6.1 0
vertex 45.1 6.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 45.1 6.9 0
vertex 45.1 6.1 4.14
vertex 45.1 6.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 45.9 6.1 0
vertex 45.9 6.9 0
vertex 45.9 6.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 45.9 6.1 0
vertex 45.9 6.9 4.14
vertex 45.9 6.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 45.1 5.1 12.39
vertex 45.9 5.1 12.39
vertex 45.9 5.9 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 45.1 5.1 12.39
vertex 45.9 5.9 12.39
vertex 45.1 5.9 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 45.1 5.1 0
vertex 45.9 5.1 0
vertex 45.9 5.1 12.39
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 45.1 5.1 0
vertex 45.9 5.1 12.39
vertex 45.1 5.1 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 45.9 5.9 0
vertex 45.1 5.9 0
vertex 45.1 5.9 12.39
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 45.9 5.9 0
vertex 45.1 5.9 12.39
vertex 45.9 5.9 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 45.1 5.9 0
vertex 45.1 5.1 0
vertex 45.1 5.1 12.39
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 45.1 5.9 0
vertex 45.1 5.1 12.39
vertex 45.1 5.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 45.9 5.1 0
vertex 45.9 5.9 0
vertex 45.9 5.9 12.39
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 45.9 5.1 0
vertex 45.9 5.9 12.39
vertex 45.9 5.1 12.39
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 45.1 4.1 8.99
vertex 45.9 4.1 8.99
vertex 45.9 4.9 8.99
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 45.1 4.1 8.99
vertex 45.9 4.9 8.99
vertex 45.1 4.9 8.99
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 45.1 4.1 0
vertex 45.9 4.1 0
vertex 45.9 4.1 8.99
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 45.1 4.1 0
vertex 45.9 4.1 8.99
vertex 45.1 4.1 8.99
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 45.9 4.9 0
vertex 45.1 4.9 0
vertex 45.1 4.9 8.99
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 45.9 4.9 0
vertex 45.1 4.9 8.99
vertex 45.9 4.9 8.99
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 45.1 4.9 0
vertex 45.1 4.1 0
vertex 45.1 4.1 8.99
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 45.1 4.9 0
vertex 45.1 4.1 8.99
vertex 45.1 4.9 8.99
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 45.9 4.1 0
vertex 45.9 4.9 0
vertex 45.9 4.9 8.99
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 45.9 4.1 0
vertex 45.9 4.9 8.99
vertex 45.9 4.1 8.99
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 45.1 3.1 4.14
vertex 45.9 3.1 4.14
vertex 45.9 3.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 45.1 3.1 4.14
vertex 45.9 3.9 4.14
vertex 45.1 3.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 45.1 3.1 0
vertex 45.9 3.1 0
vertex 45.9 3.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 45.1 3.1 0
vertex 45.9 3.1 4.14
vertex 45.1 3.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 45.9 3.9 0
vertex 45.1 3.9 0
vertex 45.1 3.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 45.9 3.9 0
vertex 45.1 3.9 4.14
vertex 45.9 3.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 45.1 3.9 0
vertex 45.1 3.1 0
vertex 45.1 3.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 45.1 3.9 0
vertex 45.1 3.1 4.14
vertex 45.1 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 45.9 3.1 0
vertex 45.9 3.9 0
vertex 45.9 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 45.9 3.1 0
vertex 45.9 3.9 4.14
vertex 45.9 3.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 47.1 6.1 5.53
vertex 47.9 6.1 5.53
vertex 47.9 6.9 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 47.1 6.1 5.53
vertex 47.9 6.9 5.53
vertex 47.1 6.9 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 47.1 6.1 0
vertex 47.9 6.1 0
vertex 47.9 6.1 5.53
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 47.1 6.1 0
vertex 47.9 6.1 5.53
vertex 47.1 6.1 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 47.9 6.9 0
vertex 47.1 6.9 0
vertex 47.1 6.9 5.53
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 47.9 6.9 0
vertex 47.1 6.9 5.53
vertex 47.9 6.9 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 47.1 6.9 0
vertex 47.1 6.1 0
vertex 47.1 6.1 5.53
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 47.1 6.9 0
vertex 47.1 6.1 5.53
vertex 47.1 6.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 47.9 6.1 0
vertex 47.9 6.9 0
vertex 47.9 6.9 5.53
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 47.9 6.1 0
vertex 47.9 6.9 5.53
vertex 47.9 6.1 5.53
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 47.1 3.1 3.16
vertex 47.9 3.1 3.16
vertex 47.9 3.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 47.1 3.1 3.16
vertex 47.9 3.9 3.16
vertex 47.1 3.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 47.1 3.1 0
vertex 47.9 3.1 0
vertex 47.9 3.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 47.1 3.1 0
vertex 47.9 3.1 3.16
vertex 47.1 3.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 47.9 3.9 0
vertex 47.1 3.9 0
vertex 47.1 3.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 47.9 3.9 0
vertex 47.1 3.9 3.16
vertex 47.9 3.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 47.1 3.9 0
vertex 47.1 3.1 0
vertex 47.1 3.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 47.1 3.9 0
vertex 47.1 3.1 3.16
vertex 47.1 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 47.9 3.1 0
vertex 47.9 3.9 0
vertex 47.9 3.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 47.9 3.1 0
vertex 47.9 3.9 3.16
vertex 47.9 3.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 47.1 2.1 6.09
vertex 47.9 2.1 6.09
vertex 47.9 2.9 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 47.1 2.1 6.09
vertex 47.9 2.9 6.09
vertex 47.1 2.9 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 47.1 2.1 0
vertex 47.9 2.1 0
vertex 47.9 2.1 6.09
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 47.1 2.1 0
vertex 47.9 2.1 6.09
vertex 47.1 2.1 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 47.9 2.9 0
vertex 47.1 2.9 0
vertex 47.1 2.9 6.09
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 47.9 2.9 0
vertex 47.1 2.9 6.09
vertex 47.9 2.9 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 47.1 2.9 0
vertex 47.1 2.1 0
vertex 47.1 2.1 6.09
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 47.1 2.9 0
vertex 47.1 2.1 6.09
vertex 47.1 2.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 47.9 2.1 0
vertex 47.9 2.9 0
vertex 47.9 2.9 6.09
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 47.9 2.1 0
vertex 47.9 2.9 6.09
vertex 47.9 2.1 6.09
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 48.1 3.1 4.14
vertex 48.9 3.1 4.14
vertex 48.9 3.9 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 48.1 3.1 4.14
vertex 48.9 3.9 4.14
vertex 48.1 3.9 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 48.1 3.1 0
vertex 48.9 3.1 0
vertex 48.9 3.1 4.14
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 48.1 3.1 0
vertex 48.9 3.1 4.14
vertex 48.1 3.1 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 48.9 3.9 0
vertex 48.1 3.9 0
vertex 48.1 3.9 4.14
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 48.9 3.9 0
vertex 48.1 3.9 4.14
vertex 48.9 3.9 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 48.1 3.9 0
vertex 48.1 3.1 0
vertex 48.1 3.1 4.14
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 48.1 3.9 0
vertex 48.1 3.1 4.14
vertex 48.1 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48.9 3.1 0
vertex 48.9 3.9 0
vertex 48.9 3.9 4.14
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 48.9 3.1 0
vertex 48.9 3.9 4.14
vertex 48.9 3.1 4.14
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 49.1 1.1 7.49
vertex 49.9 1.1 7.49
vertex 49.9 1.9 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 49.1 1.1 7.49
vertex 49.9 1.9 7.49
vertex 49.1 1.9 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 49.1 1.1 0
vertex 49.9 1.1 0
vertex 49.9 1.1 7.49
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 49.1 1.1 0
vertex 49.9 1.1 7.49
vertex 49.1 1.1 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 49.9 1.9 0
vertex 49.1 1.9 0
vertex 49.1 1.9 7.49
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 49.9 1.9 0
vertex 49.1 1.9 7.49
vertex 49.9 1.9 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 49.1 1.9 0
vertex 49.1 1.1 0
vertex 49.1 1.1 7.49
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 49.1 1.9 0
vertex 49.1 1.1 7.49
vertex 49.1 1.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 49.9 1.1 0
vertex 49.9 1.9 0
vertex 49.9 1.9 7.49
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 49.9 1.1 0
vertex 49.9 1.9 7.49
vertex 49.9 1.1 7.49
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 50.1 4.1 3.16
vertex 50.9 4.1 3.16
vertex 50.9 4.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 50.1 4.1 3.16
vertex 50.9 4.9 3.16
vertex 50.1 4.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 50.1 4.1 0
vertex 50.9 4.1 0
vertex 50.9 4.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 50.1 4.1 0
vertex 50.9 4.1 3.16
vertex 50.1 4.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 50.9 4.9 0
vertex 50.1 4.9 0
vertex 50.1 4.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 50.9 4.9 0
vertex 50.1 4.9 3.16
vertex 50.9 4.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 50.1 4.9 0
vertex 50.1 4.1 0
vertex 50.1 4.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 50.1 4.9 0
vertex 50.1 4.1 3.16
vertex 50.1 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 50.9 4.1 0
vertex 50.9 4.9 0
vertex 50.9 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 50.9 4.1 0
vertex 50.9 4.9 3.16
vertex 50.9 4.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 51.1 2.1 4.9
vertex 51.9 2.1 4.9
vertex 51.9 2.9 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 51.1 2.1 4.9
vertex 51.9 2.9 4.9
vertex 51.1 2.9 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 51.1 2.1 0
vertex 51.9 2.1 0
vertex 51.9 2.1 4.9
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 51.1 2.1 0
vertex 51.9 2.1 4.9
vertex 51.1 2.1 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 51.9 2.9 0
vertex 51.1 2.9 0
vertex 51.1 2.9 4.9
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 51.9 2.9 0
vertex 51.1 2.9 4.9
vertex 51.9 2.9 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 51.1 2.9 0
vertex 51.1 2.1 0
vertex 51.1 2.1 4.9
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 51.1 2.9 0
vertex 51.1 2.1 4.9
vertex 51.1 2.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 51.9 2.1 0
vertex 51.9 2.9 0
vertex 51.9 2.9 4.9
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 51.9 2.1 0
vertex 51.9 2.9 4.9
vertex 51.9 2.1 4.9
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 51.1 1.1 17.52
vertex 51.9 1.1 17.52
vertex 51.9 1.9 17.52
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 51.1 1.1 17.52
vertex 51.9 1.9 17.52
vertex 51.1 1.9 17.52
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 51.1 1.1 0
vertex 51.9 1.1 0
vertex 51.9 1.1 17.52
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 51.1 1.1 0
vertex 51.9 1.1 17.52
vertex 51.1 1.1 17.52
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 51.9 1.9 0
vertex 51.1 1.9 0
vertex 51.1 1.9 17.52
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 51.9 1.9 0
vertex 51.1 1.9 17.52
vertex 51.9 1.9 17.52
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 51.1 1.9 0
vertex 51.1 1.1 0
vertex 51.1 1.1 17.52
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 51.1 1.9 0
vertex 51.1 1.1 17.52
vertex 51.1 1.9 17.52
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 51.9 1.1 0
vertex 51.9 1.9 0
vertex 51.9 1.9 17.52
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 51.9 1.1 0
vertex 51.9 1.9 17.52
vertex 51.9 1.1 17.52
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 51.1 0.1 6.59
vertex 51.9 0.1 6.59
vertex 51.9 0.9 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 51.1 0.1 6.59
vertex 51.9 0.9 6.59
vertex 51.1 0.9 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 51.1 0.1 0
vertex 51.9 0.1 0
vertex 51.9 0.1 6.59
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 51.1 0.1 0
vertex 51.9 0.1 6.59
vertex 51.1 0.1 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 51.9 0.9 0
vertex 51.1 0.9 0
vertex 51.1 0.9 6.59
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 51.9 0.9 0
vertex 51.1 0.9 6.59
vertex 51.9 0.9 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 51.1 0.9 0
vertex 51.1 0.1 0
vertex 51.1 0.1 6.59
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 51.1 0.9 0
vertex 51.1 0.1 6.59
vertex 51.1 0.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 51.9 0.1 0
vertex 51.9 0.9 0
vertex 51.9 0.9 6.59
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 51.9 0.1 0
vertex 51.9 0.9 6.59
vertex 51.9 0.1 6.59
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 52.1 6.1 9.33
vertex 52.9 6.1 9.33
vertex 52.9 6.9 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 52.1 6.1 9.33
vertex 52.9 6.9 9.33
vertex 52.1 6.9 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 52.1 6.1 0
vertex 52.9 6.1 0
vertex 52.9 6.1 9.33
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 52.1 6.1 0
vertex 52.9 6.1 9.33
vertex 52.1 6.1 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 52.9 6.9 0
vertex 52.1 6.9 0
vertex 52.1 6.9 9.33
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 52.9 6.9 0
vertex 52.1 6.9 9.33
vertex 52.9 6.9 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 52.1 6.9 0
vertex 52.1 6.1 0
vertex 52.1 6.1 9.33
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 52.1 6.9 0
vertex 52.1 6.1 9.33
vertex 52.1 6.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 52.9 6.1 0
vertex 52.9 6.9 0
vertex 52.9 6.9 9.33
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 52.9 6.1 0
vertex 52.9 6.9 9.33
vertex 52.9 6.1 9.33
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 52.1 4.1 3.16
vertex 52.9 4.1 3.16
vertex 52.9 4.9 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 52.1 4.1 3.16
vertex 52.9 4.9 3.16
vertex 52.1 4.9 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 52.1 4.1 0
vertex 52.9 4.1 0
vertex 52.9 4.1 3.16
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 52.1 4.1 0
vertex 52.9 4.1 3.16
vertex 52.1 4.1 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 52.9 4.9 0
vertex 52.1 4.9 0
vertex 52.1 4.9 3.16
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 52.9 4.9 0
vertex 52.1 4.9 3.16
vertex 52.9 4.9 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 52.1 4.9 0
vertex 52.1 4.1 0
vertex 52.1 4.1 3.16
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 52.1 4.9 0
vertex 52.1 4.1 3.16
vertex 52.1 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 52.9 4.1 0
vertex 52.9 4.9 0
vertex 52.9 4.9 3.16
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 52.9 4.1 0
vertex 52.9 4.9 3.16
vertex 52.9 4.1 3.16
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 52.1 3.1 9.96
vertex 52.9 3.1 9.96
vertex 52.9 3.9 9.96
endloop
endfacet
facet normal 0 0 1
outer loop
vertex 52.1 3.1 9.96
vertex 52.9 3.9 9.96
vertex 52.1 3.9 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 52.1 3.1 0
vertex 52.9 3.1 0
vertex 52.9 3.1 9.96
endloop
endfacet
facet normal 0 -1 0
outer loop
vertex 52.1 3.1 0
vertex 52.9 3.1 9.96
vertex 52.1 3.1 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 52.9 3.9 0
vertex 52.1 3.9 0
vertex 52.1 3.9 9.96
endloop
endfacet
facet normal 0 1 0
outer loop
vertex 52.9 3.9 0
vertex 52.1 3.9 9.96
vertex 52.9 3.9 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 52.1 3.9 0
vertex 52.1 3.1 0
vertex 52.1 3.1 9.96
endloop
endfacet
facet normal -1 0 0
outer loop
vertex 52.1 3.9 0
vertex 52.1 3.1 9.96
vertex 52.1 3.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 52.9 3.1 0
vertex 52.9 3.9 0
vertex 52.9 3.9 9.96
endloop
endfacet
facet normal 1 0 0
outer loop
vertex 52.9 3.1 0
vertex 52.9 3.9 9.96
vertex 52.9 3.1 9.96
endloop
endfacet
endsolid contributions
```
<!-- skyline:end -->

### Focus

- **LLM applications** — structured extraction with LLMs, tool-calling assistants, LoRA / QLoRA fine-tuning
- **Computer vision** — semantic segmentation (DeepLabV3+, U-Net, Attention U-Net), image embeddings for retrieval
- **Recommender systems** — hybrid content + collaborative ranking, diversification, cold start, offline evaluation
- **ML in production** — FastAPI services, background jobs, Docker Compose deployments, the frontend that uses the model

### Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img alt="Stack as a model summary: LLM, vision, ranking, serving and product layers with their tools" src="assets/stack-light.svg" width="100%">
</picture>

<details>
<summary>Plain-text stack</summary>
<br>

**LLM** · Transformers · PEFT / LoRA · bitsandbytes · OpenAI, Claude and Gemini APIs  
**Vision** · PyTorch · segmentation-models-pytorch · OpenCV · CLIP · Albumentations  
**Ranking** · scikit-learn · implicit (ALS) · sentence-transformers · XGBoost  
**Serving** · FastAPI · Docker · PostgreSQL · SQLite · nginx  
**Product** · TypeScript · React · Next.js · Tailwind

</details>

### Latest commits

<a href="https://github.com/vadimtkacj1?tab=repositories">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/recent-dark.svg">
    <img alt="Latest commits across the showcase repositories" src="assets/recent-light.svg" width="100%">
  </picture>
</a>
