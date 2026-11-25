import RandomKripke.ChainFrames

namespace RandomKripke

/-- The noncentral source vertices of a candidate fibre map. -/
def chainNoncentral {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) : Finset α :=
  Finset.univ.filter (fun x => (f x).val ≠ 0)

def chainOddVertices {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) : Finset α :=
  (chainNoncentral r f).filter (fun x => (f x).val % 2 = 1)

def chainEvenVertices {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) : Finset α :=
  (chainNoncentral r f).filter (fun x => ¬ (f x).val % 2 = 1)

/-- Ordered noncentral pairs permitted by the target relation. -/
def chainAllowedPairs {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) : Finset (α × α) :=
  ((chainNoncentral r f).product (chainNoncentral r f)).filter
    (fun p => (f p.2).val = (f p.1).val + 1)

/-- The complementary ordered noncentral pairs, including prohibited loops. -/
def chainForbiddenPairs {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) : Finset (α × α) :=
  ((chainNoncentral r f).product (chainNoncentral r f)).filter
    (fun p => ¬ (f p.2).val = (f p.1).val + 1)

/-- Orient a pair so its odd-labelled endpoint comes first. -/
def chainOrient {α : Type} (r : ℕ) (f : α → Fin (r + 1))
    (p : α × α) : α × α :=
  if (f p.1).val % 2 = 1 then p else (p.2, p.1)

theorem chain_vertex_parity_card {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) :
    (chainOddVertices r f).card + (chainEvenVertices r f).card =
      (chainNoncentral r f).card := by
  unfold chainOddVertices chainEvenVertices
  exact Finset.card_filter_add_card_filter_not _

theorem chain_pair_card_total {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) :
    (chainAllowedPairs r f).card + (chainForbiddenPairs r f).card =
      (chainNoncentral r f).card ^ 2 := by
  unfold chainAllowedPairs chainForbiddenPairs
  rw [Finset.card_filter_add_card_filter_not, Finset.card_product, pow_two]

theorem chain_allowed_orient_mem {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) (p : α × α)
    (hp : p ∈ chainAllowedPairs r f) :
    chainOrient r f p ∈ (chainOddVertices r f).product (chainEvenVertices r f) := by
  have h := Finset.mem_filter.mp hp
  have hmem := Finset.mem_product.mp h.1
  have hsucc := h.2
  by_cases ho : (f p.1).val % 2 = 1
  · have he : ¬ (f p.2).val % 2 = 1 := by omega
    simp only [chainOrient, if_pos ho, Finset.mem_product,
      chainOddVertices, chainEvenVertices, Finset.mem_filter]
    exact ⟨⟨hmem.1, ho⟩, ⟨hmem.2, he⟩⟩
  · have he : (f p.2).val % 2 = 1 := by omega
    simp only [chainOrient, if_neg ho, Finset.mem_product,
      chainOddVertices, chainEvenVertices, Finset.mem_filter]
    exact ⟨⟨hmem.2, he⟩, ⟨hmem.1, ho⟩⟩

theorem chain_allowed_orient_injective {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) :
    Set.InjOn (chainOrient r f) (↑(chainAllowedPairs r f) : Set (α × α)) := by
  intro p hp q hq heq
  have hp' : p ∈ chainAllowedPairs r f := hp
  have hq' : q ∈ chainAllowedPairs r f := hq
  have hpSucc := (Finset.mem_filter.mp hp').2
  have hqSucc := (Finset.mem_filter.mp hq').2
  by_cases hpo : (f p.1).val % 2 = 1 <;>
    by_cases hqo : (f q.1).val % 2 = 1
  · simpa only [chainOrient, if_pos hpo, if_pos hqo] using heq
  · simp only [chainOrient, if_pos hpo, if_neg hqo] at heq
    have h1 := congrArg (fun t : α × α => (f t.1).val) heq
    have h2 := congrArg (fun t : α × α => (f t.2).val) heq
    change (f p.1).val = (f q.2).val at h1
    change (f p.2).val = (f q.1).val at h2
    omega
  · simp only [chainOrient, if_neg hpo, if_pos hqo] at heq
    have h1 := congrArg (fun t : α × α => (f t.1).val) heq
    have h2 := congrArg (fun t : α × α => (f t.2).val) heq
    change (f p.2).val = (f q.1).val at h1
    change (f p.1).val = (f q.2).val at h2
    omega
  · simp only [chainOrient, if_neg hpo, if_neg hqo] at heq
    exact Prod.ext (congrArg Prod.snd heq) (congrArg Prod.fst heq)

theorem chain_allowed_card_le_parity_product {α : Type} [Fintype α]
    (r : ℕ) (f : α → Fin (r + 1)) :
    (chainAllowedPairs r f).card ≤
      (chainOddVertices r f).card * (chainEvenVertices r f).card := by
  classical
  have hsub :
      (chainAllowedPairs r f).image (chainOrient r f) ⊆
        (chainOddVertices r f).product (chainEvenVertices r f) := by
    intro z hz
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hz
    exact chain_allowed_orient_mem r f p hp
  have hle := Finset.card_le_card hsub
  rw [Finset.card_image_of_injOn (chain_allowed_orient_injective r f),
    Finset.card_product] at hle
  exact hle

/-- Actual cardinality estimate for the forbidden ordered pairs. It
does not require surjectivity, nor that all fibres are nonempty. -/
theorem chain_forbidden_pairs_card_lower {α : Type} [Fintype α] (r : ℕ)
    (f : α → Fin (r + 1)) :
    3 * (chainNoncentral r f).card ^ 2 ≤
      4 * (chainForbiddenPairs r f).card := by
  have hA := chain_allowed_card_le_parity_product r f
  have hP := chain_four_product_le_square
    (chainOddVertices r f).card (chainEvenVertices r f).card
  rw [chain_vertex_parity_card r f] at hP
  have hQ := chain_pair_card_total r f
  omega

/-- A bounded morphism forces every pair in the forbidden set to be absent. -/
theorem boundedMorphism_chain_forbidden_pairs_absent
    {α : Type} [Fintype α] (r : ℕ) (R : Frame α)
    (f : α → Fin (r + 1)) (h : IsBoundedMorphism R (ChainFrame r) f)
    (p : α × α) (hp : p ∈ chainForbiddenPairs r f) :
    R p.1 p.2 = false := by
  have hpair := Finset.mem_filter.mp hp
  have hmem := Finset.mem_product.mp hpair.1
  have hx := (Finset.mem_filter.mp hmem.1).2
  have hy := (Finset.mem_filter.mp hmem.2).2
  exact (boundedMorphism_chain_implies_witness r R f h).2.1
    p.1 p.2 hx hy hpair.2

end RandomKripke
