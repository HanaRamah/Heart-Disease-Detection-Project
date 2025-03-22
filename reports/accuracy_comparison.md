# Decision Tree vs Expert System for Heart Disease Prediction

## 1. Validation Set Evaluation:
### Decision Tree:
- Evaluated using unseen data (test set).
- Uses metrics like accuracy, precision, recall, and F1-score for performance evaluation.

### Expert System:
- Based on predefined rules (no traditional testing set).
- Evaluation based on the application of rules and the correctness of risk level assessment.

## 2. Accuracy Comparison:
### Decision Tree Model:
- Accuracy: 0.98
- Precision: 0.99
- Recall: 0.97
- F1-Score: 0.98
### Expert System:
- Risk levels (e.g., High, Moderate, Low) determined by rules.
- No direct accuracy comparison as it is rule-based, but performs well in correctly identifying risk levels based on user input.

## 3. Explainability:
### Decision Tree:
- High interpretability with visualized tree structure.
- Clear explanation of decision-making process.

### Expert System:
- Rules are explicitly defined and easy to explain.
- Rigid and fixed; cannot adapt automatically to new data without modification.

## 4. Performance Comparison:

| Metric               | Decision Tree Model        | Expert System           |
|----------------------|----------------------------|-------------------------|
| **Accuracy**         | 98%                        | N/A (Rule-based)        |
| **Precision**        | 99%                      | N/A (Rule-based)        |
| **Recall**           | 97%                      | N/A (Rule-based)        |
| **F1-Score**         | 98%                      | N/A (Rule-based)        |
| **Explainability**   | High (Tree visualization)  | High (Rule clarity)     |

## 5. Conclusion:
- **Decision Tree** performs better in terms of measurable performance metrics.
- **Expert System** is more interpretable and customizable but lacks adaptability to new data without manual updates.
