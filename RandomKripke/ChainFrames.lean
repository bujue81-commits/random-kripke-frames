import RandomKripke.FiniteFrames

namespace RandomKripke

/-- The target from Goranko (2020), Proposition 4.7:
0 is central, and the only noncentral edges are i → i+1. -/
def ChainFrame (r : ℕ) : Frame (Fin (r + 1)) :=
  fun i j => decide (i.val = 0 ∨ j.val = 0 ∨ j.val = i.val + 1)

/-- The selected necessary event used by the chain first-moment proof. -/
def ChainWitnessConditions {α : Type} (r : ℕ)
    (R : Frame α) (f : α → Fin (r + 1)) : Prop :=
  Function.Surjective f ∧
    (∀ x y, (f x).val ≠ 0 → (f y).val ≠ 0 →
      (f y).val ≠ (f x).val + 1 → R x y = false) ∧
    (∀ x, (f x).val = 0 → ∀ j : Fin (r + 1), j.val ≠ 0 →
      ∃ y, R x y = true ∧ f y = j)

theorem boundedMorphism_chain_implies_witness
    {α : Type} (r : ℕ) (R : Frame α) (f : α → Fin (r + 1)) :
    IsBoundedMorphism R (ChainFrame r) f → ChainWitnessConditions r R f := by
  rintro ⟨hs, hforth, hback⟩
  refine ⟨hs, ?_, ?_⟩
  · intro x y hx hy hnext
    cases hxy : R x y with
    | false => rfl
    | true =>
        have h := hforth x y hxy
        simp [ChainFrame, hx, hy, hnext] at h
  · intro x hx j hj
    have htarget : ChainFrame r (f x) j = true := by
      simp [ChainFrame, hx]
    exact hback x j htarget

/-- Adjacent products for an ordered list of noncentral fibre sizes. -/
def chainAdjacentWeight : List ℕ → ℕ
  | [] => 0
  | a :: xs => a * xs.headD 0 + chainAdjacentWeight xs

/-- Sums of the odd and even positions, counting positions from one. -/
def chainParitySums : List ℕ → ℕ × ℕ
  | [] => (0, 0)
  | a :: xs => (a + (chainParitySums xs).2, (chainParitySums xs).1)

theorem chain_head_le_odd (xs : List ℕ) :
    xs.headD 0 ≤ (chainParitySums xs).1 := by
  cases xs with
  | nil => decide
  | cons a xs =>
      change a ≤ a + (chainParitySums xs).2
      omega

theorem chain_parity_total (xs : List ℕ) :
    (chainParitySums xs).1 + (chainParitySums xs).2 = xs.sum := by
  induction xs with
  | nil => rfl
  | cons a xs ih =>
      change (a + (chainParitySums xs).2) + (chainParitySums xs).1 =
        a + xs.sum
      omega

theorem chain_adjacent_le_parity_product (xs : List ℕ) :
    chainAdjacentWeight xs ≤ (chainParitySums xs).1 * (chainParitySums xs).2 := by
  induction xs with
  | nil => decide
  | cons a xs ih =>
      change a * xs.headD 0 + chainAdjacentWeight xs ≤
        (a + (chainParitySums xs).2) * (chainParitySums xs).1
      calc
        _ ≤ a * (chainParitySums xs).1 +
            (chainParitySums xs).1 * (chainParitySums xs).2 :=
          Nat.add_le_add (Nat.mul_le_mul_left a (chain_head_le_odd xs)) ih
        _ = _ := by ring

theorem chain_four_product_le_square (u v : ℕ) :
    4 * (u * v) ≤ (u + v)^2 := by
  have h : (4 : ℤ) * ((u : ℤ) * (v : ℤ)) ≤ ((u : ℤ) + (v : ℤ))^2 := by
    nlinarith [sq_nonneg ((u : ℤ) - (v : ℤ))]
  exact_mod_cast h

theorem chain_four_adjacent_le_square (xs : List ℕ) :
    4 * chainAdjacentWeight xs ≤ xs.sum^2 := by
  calc
    _ ≤ 4 * ((chainParitySums xs).1 * (chainParitySums xs).2) :=
      Nat.mul_le_mul_left 4 (chain_adjacent_le_parity_product xs)
    _ ≤ ((chainParitySums xs).1 + (chainParitySums xs).2)^2 :=
      chain_four_product_le_square _ _
    _ = _ := by rw [chain_parity_total xs]

/-- Arithmetic part of the forbidden-edge estimate: 4Q ≥ 3S².
The identification of Q with a cardinality of forbidden ordered pairs
for an actual partition is a separate combinatorial milestone. -/
theorem chain_forbidden_weight_lower (xs : List ℕ) :
    3 * xs.sum^2 ≤ 4 * (xs.sum^2 - chainAdjacentWeight xs) := by
  have h := chain_four_adjacent_le_square xs
  omega

end RandomKripke
