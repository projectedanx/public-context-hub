<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Design the canonical ontology schema for Neo4j

```json
{
  "Hickam_Orientation": {
    "Occam_Reject": "I have rejected the simple explanation that the Neo4j design should be a plain paper-to-entity graph, because the file argues that the product's real moat is translation across epistemic frames rather than generic retrieval. [file:1]",
    "Comorbid_Factors": [
      "Factor A: The file explicitly proposes a canonical intermediate schema of Document, Discipline, Concept, Method, Claim, Evidence, Assumption, Metric, Dataset, Mapping, and Hypothesis. [file:1]",
      "Factor B: The review corpus says assumptions must become first-class objects and that every mapping should be treated as a lossy transformation with a Translation Loss Score. [file:1]",
      "Factor C: The product plan separates the relational layer, graph layer, and vector layer, which means Neo4j should hold the reasoning substrate, not all application state. [file:1]"
    ]
  },
  "Contrastive_Delta": {
    "Amateur_Impulse": "The generic response would be to model Documents, Concepts, and Methods as nodes with a few direct edges and stop there. [file:1]",
    "Inductive_Synthesis": "Aggregating the document's critiques reveals that a usable schema must encode provenance, assumptions, evidence preferences, and imperfect cross-domain mappings, otherwise the graph becomes a semantic blob. [file:1]",
    "Abductive_Leap": "The most structurally isomorphic design is a translation-first ontology in which Mapping is a reified node carrying loss, compatibility, and confidence, while Concept, Method, Claim, and Assumption carry epistemic contracts. [file:1]",
    "Expert_Correction": "Therefore, the schema below treats Neo4j as an epistemic translation engine, not just a citation graph. [file:1]"
  },
  "Martensite_Metrics": {
    "Aesthetic_Tension": "High. [file:1]",
    "Intent_Divergence_Risk": "Safe. [file:1]",
    "Twinning_Mechanism": "I am stabilizing the design by keeping the core object set from the file, while adding only the minimum supporting nodes needed for provenance and queryability. [file:1]"
  }
}
```


***

Yes — the right Neo4j design here is a **translation-first ontology**, not a generic literature graph: make `Document`, `Discipline`, `Concept`, `Method`, `Claim`, `Evidence`, `Assumption`, `Metric`, `Dataset`, `Mapping`, and `Hypothesis` first-class nodes, and treat mappings as scored, lossy objects rather than simple edges.[^1]
That follows the strongest guidance in the file: represent assumptions explicitly, separate evidence-backed structure from generated synthesis, and encode how concepts translate imperfectly across disciplines.[^1]

## Core model

The file already gives the canonical object set, so I would use that as the stable semantic backbone and keep user/workspace/billing state in PostgreSQL, not Neo4j.[^1]
I would also make `Mapping` the central reified object, because the file says cross-domain alignment must carry translation loss, methodological compatibility, assumption divergence, and confidence instead of pretending that two concepts are simply equivalent.[^1]

**Design rules**[^1]

- Provenance first: every extracted claim, method, and assumption should point back to a document passage or source context.[^1]
- Assumptions first-class: do not bury epistemic stance inside free text, because the file treats assumption surfacing as a core product feature.[^1]
- Lossy translation explicit: support `exact`, `partial`, `analogy-only`, and `conflict` mappings, because the file flags ontology drift and false equivalence as major implementation risks.[^1]
- Evidence separate from hypothesis: the file explicitly says to separate retrieved support from generated hypotheses to reduce hallucinated analogies.[^1]


## Node labels

I would use the following **authoritative node set** in Neo4j.[^1]


| Label | Purpose | Key properties |
| :-- | :-- | :-- |
| `Document` [^1] | Source artifact ingested into the system. [^1] | `id`, `title`, `year`, `doi`, `source_url`, `doc_type`, `discipline_guess`, `ingestion_confidence` |
| `Discipline` [^1] | Domain frame used to contextualize concepts and evidence norms. [^1] | `id`, `name`, `parent_domain`, `description` |
| `Concept` [^1] | Transferable or non-transferable construct in a field. [^1] | `id`, `canonical_name`, `aliases`, `definition`, `ontology_type`, `epistemology`, `scale`, `measurement_mode`, `extraction_confidence` |
| `Method` [^1] | Analytical or experimental technique. [^1] | `id`, `name`, `method_family`, `data_structure`, `quant_mode`, `scale`, `requirements`, `extraction_confidence` |
| `Claim` [^1] | Atomic statement extracted from a source. [^1] | `id`, `text`, `claim_type`, `polarity`, `confidence`, `novelty_flag` |
| `Assumption` [^1] | Ontological, epistemological, or methodological stance. [^1] | `id`, `text`, `assumption_type`, `stance_axis`, `strength`, `explicitness` |
| `Evidence` [^1] | Supporting empirical or theoretical backing. [^1] | `id`, `evidence_type`, `strength`, `sample_size`, `reproducibility`, `confidence` |
| `Metric` [^1] | Measured variable or evaluation criterion. [^1] | `id`, `name`, `unit`, `level_of_measurement`, `aggregation_level` |
| `Dataset` [^1] | Data source used by evidence or method. [^1] | `id`, `name`, `modality`, `granularity`, `access_type`, `schema_hint` |
| `Mapping` [^1] | Reified cross-domain translation object. [^1] | `id`, `mapping_type`, `translation_loss`, `structural_similarity`, `methodological_compatibility`, `assumption_divergence`, `confidence`, `status`, `rationale` |
| `Hypothesis` [^1] | Generated synthesis proposal or “Third Realm” idea. [^1] | `id`, `text`, `mode`, `novelty_score`, `feasibility_score`, `synthesis_depth`, `status` |

I would add two **supporting nodes** that the file strongly implies even though they are not in the original core list: `Passage` for citation-grade provenance, because the file repeatedly requires grounded support and source passages, and `ProblemType` because the file gives `METHOD -> APPLICABLE_TO -> PROBLEM_TYPE` as an example relation.[^1]

## Relationship model

The file already names several canonical relations, and I would turn them into the baseline traversal grammar below.[^1]

**Source and provenance**[^1]

- `(:Document)-[:BELONGS_TO]->(:Discipline)`[^1]
- `(:Document)-[:HAS_PASSAGE]->(:Passage)`[^1]
- `(:Document)-[:CONTAINS]->(:Claim)`[^1]
- `(:Claim)-[:EXPRESSED_IN]->(:Passage)`[^1]

**Reasoning substrate**[^1]

- `(:Claim)-[:ABOUT]->(:Concept)`[^1]
- `(:Claim)-[:USES]->(:Method)`[^1]
- `(:Claim)-[:ASSUMES]->(:Assumption)`[^1]
- `(:Claim)-[:SUPPORTED_BY]->(:Evidence)`[^1]
- `(:Evidence)-[:FROM_DATASET]->(:Dataset)`[^1]
- `(:Evidence)-[:MEASURED_BY]->(:Metric)`[^1]
- `(:Discipline)-[:PRIORITIZES]->(:EvidenceType)` or `(:Discipline)-[:PRIORITIZES]->(:Evidence)` depending on whether you want a controlled taxonomy or empirical observations.[^1]

**Transfer and synthesis**[^1]

- `(:Method)-[:APPLICABLE_TO]->(:ProblemType)`[^1]
- `(:Concept)-[:RELATED_TO]->(:Concept)` for within-discipline structure, but not for authoritative translation.[^1]
- `(:Mapping)-[:SOURCE]->(:Concept|Method|Claim|Assumption)` [^1]
- `(:Mapping)-[:TARGET]->(:Concept|Method|Claim|Assumption)` [^1]
- `(:Mapping)-[:SUPPORTED_BY]->(:Evidence|Claim|Passage)` [^1]
- `(:Hypothesis)-[:DERIVED_FROM]->(:Mapping)`[^1]
- `(:Hypothesis)-[:SYNTHESIZES]->(:Concept|Method|Assumption)` [^1]

The key move is **not** to store the authoritative cross-domain translation as a plain `:ALIGNS_WITH` edge, because the file says mappings are lossy and must expose where the analogy holds and where it breaks.[^1]
If you want query speed, you can materialize derived shortcut edges such as `:ALIGNS_WITH` or `:CAN_TRANSFER_TO`, but treat them as cacheable views regenerated from `Mapping` nodes rather than as the source of truth.[^1]

## Epistemic contract

The file’s most important critique is that cross-domain entities cannot be aligned safely unless the graph stores their **epistemic contract**.[^1]
I would therefore require the following shared properties on `Concept`, `Method`, `Claim`, and `Assumption`, with some optional overlap on `Evidence`.[^1]

**Required contract fields**[^1]

- `ontology_type`: `construct | observable | latent_variable | simulation_artifact` [^1]
- `epistemology`: `empirical | theoretical | interpretive | mixed` [^1]
- `measurement_mode`: `quantitative_proxy | qualitative_coding | simulation | formal_derivation | observational` [^1]
- `scale`: `micro | meso | macro | multi_scale` [^1]
- `disciplinary_frame`: free-text or controlled tag such as `sociology`, `information_theory`, `cognitive_science`[^1]
- `confidence`: extraction or curation confidence, because the file calls for schema validation and confidence scoring.[^1]

For `Mapping`, I would define the **Translation Loss Score** exactly as the file suggests: store `structural_similarity`, `methodological_compatibility`, and `assumption_divergence`, then compute `translation_loss` as a normalized aggregate used to classify the result as `high_fidelity`, `analogy_only`, or `invalid_transfer`.[^1]
I would also add `mapping_type` values of `exact`, `partial`, `analogy_only`, and `conflict`, because that directly answers the ontology-drift mitigation proposed in the file.[^1]

## Cypher baseline

This is the minimum Neo4j DDL I would start with for the canonical schema.[^1]

```cypher
CREATE CONSTRAINT document_id IF NOT EXISTS
FOR (n:Document) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT discipline_id IF NOT EXISTS
FOR (n:Discipline) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT concept_id IF NOT EXISTS
FOR (n:Concept) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT method_id IF NOT EXISTS
FOR (n:Method) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT claim_id IF NOT EXISTS
FOR (n:Claim) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT assumption_id IF NOT EXISTS
FOR (n:Assumption) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT evidence_id IF NOT EXISTS
FOR (n:Evidence) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT metric_id IF NOT EXISTS
FOR (n:Metric) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT dataset_id IF NOT EXISTS
FOR (n:Dataset) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT mapping_id IF NOT EXISTS
FOR (n:Mapping) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT hypothesis_id IF NOT EXISTS
FOR (n:Hypothesis) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT passage_id IF NOT EXISTS
FOR (n:Passage) REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT problemtype_id IF NOT EXISTS
FOR (n:ProblemType) REQUIRE n.id IS UNIQUE;

CREATE INDEX concept_name IF NOT EXISTS
FOR (n:Concept) ON (n.canonical_name);

CREATE INDEX method_name IF NOT EXISTS
FOR (n:Method) ON (n.name);

CREATE INDEX assumption_type IF NOT EXISTS
FOR (n:Assumption) ON (n.assumption_type);

CREATE INDEX mapping_status IF NOT EXISTS
FOR (n:Mapping) ON (n.status);

CREATE FULLTEXT INDEX semantic_lookup IF NOT EXISTS
FOR (n:Concept|Method|Claim|Assumption|Hypothesis)
ON EACH [n.canonical_name, n.name, n.text, n.definition, n.rationale];
```

I would insert mappings with a reified pattern like this, because the file’s critique depends on storing scores and provenance on the mapping itself.[^1]

```cypher
MERGE (src:Concept {id: $source_id})
MERGE (tgt:Concept {id: $target_id})
MERGE (m:Mapping {id: $mapping_id})
SET m.mapping_type = $mapping_type,
    m.translation_loss = $translation_loss,
    m.structural_similarity = $structural_similarity,
    m.methodological_compatibility = $methodological_compatibility,
    m.assumption_divergence = $assumption_divergence,
    m.confidence = $confidence,
    m.status = $status,
    m.rationale = $rationale
MERGE (m)-[:SOURCE]->(src)
MERGE (m)-[:TARGET]->(tgt);
```

A useful retrieval query for the “Rosetta Stone” feature would rank methods by low translation loss and low assumption divergence rather than by embedding similarity alone, because the file explicitly argues for constraint-aware retrieval over naive nearest-neighbor matching.[^1]

```cypher
MATCH (c:Concept {canonical_name: $problem_concept})<-[:ABOUT]-(:Claim)-[:USES]->(m1:Method)
MATCH (map:Mapping)-[:SOURCE]->(m1)
MATCH (map)-[:TARGET]->(m2:Method)
WHERE map.translation_loss < 0.35
  AND map.assumption_divergence < 0.30
RETURN m1.name AS source_method,
       m2.name AS candidate_method,
       map.mapping_type AS mapping_type,
       map.translation_loss AS translation_loss,
       map.confidence AS confidence,
       map.rationale AS rationale
ORDER BY map.translation_loss ASC, map.confidence DESC
LIMIT 20;
```


## Operational notes

Keep Neo4j focused on the **reasoning substrate** and let PostgreSQL hold users, organizations, workspaces, permissions, report history, and billing, because the file explicitly separates those layers.[^1]
For embeddings, the file recommends `PostgreSQL + pgvector + Neo4j` as the simpler MVP stack, so I would store only `embedding_ref` or compact search fields in Neo4j and let pgvector handle primary semantic retrieval until scale forces a dedicated vector database.[^1]

The most important anti-pattern to avoid is collapsing `Concept`, `Method`, `Assumption`, and `Claim` into one generic `Entity` label, because the file’s whole design logic depends on distinguishing what a field studies, how it studies it, what it asserts, and what it presupposes.[^1]
The second anti-pattern is treating cross-domain alignment as a binary edge, because the file repeatedly warns that elegant but false analogies are the central failure mode of the product.[^1]

Would you like this turned into a full **Neo4j schema package** next — with label definitions, Cypher migrations, seed vocabularies, and 10 canonical query recipes?

<div align="center">⁂</div>

[^1]: paste.txt

