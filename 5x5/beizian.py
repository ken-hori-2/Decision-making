import matplotlib
import matplotlib.pyplot as plt
import networkx as nx

from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel

model = BayesianModel([
    # ('親ノード', '子ノード')
    ('battery', 'gauge'),
    ('fuel', 'gauge'),
])

battery_cpd = TabularCPD(
    variable='battery',
    variable_card=2,
    # values[0]: empty, values[1]: full
    values=[[.1], [.9]])
print(battery_cpd)

fuel_cpd = TabularCPD(
    variable='fuel',
    variable_card=2,
    # values[0]: empty, values[1]: full
    values=[[.1], [.9]])
print(fuel_cpd)

# valuesの与え方は以下のドキュメント参照
# https://pgmpy.org/models.html#module-pgmpy.models.BayesianModel
gauge_cpd = TabularCPD(
    variable='gauge',
    variable_card=2,
    values = [[.9, .8, .8, .2],
             [.1, .2, .2, .8]],
    evidence = ['battery', 'fuel'],
    evidence_card=[2, 2]
)
print(gauge_cpd)

# CPDをモデルに与える
model.add_cpds(battery_cpd, fuel_cpd, gauge_cpd)

# CPDを与えたモデルが有効かチェック
model.check_model()

# モデルの構造可視化
nx.draw(model, with_labels=True)
plt.show()

model.get_independencies()

model_infer = VariableElimination(model)

# 確認
battery_prob = model_infer.query(variables=['battery'])
print(battery_prob)

fuel_prob = model_infer.query(variables=['fuel'])
print(fuel_prob)

battery_fuel_prob = model_infer.query(variables=['battery', 'fuel', 'gauge'])
print(battery_fuel_prob)

gauge_prob = model_infer.query(variables=['gauge'])
print(gauge_prob)

fuel0_prob_given_gauge0 = model_infer.query(variables=['fuel'], evidence={'gauge': 0})
print(fuel0_prob_given_gauge0)

print(fuel0_prob_given_gauge0.values[0])

fuel0_prob_given_gauge0_battery0 = model_infer.query(variables=['fuel'], evidence={'gauge': 0, 'battery': 0})
print(fuel0_prob_given_gauge0_battery0)

plt.show()