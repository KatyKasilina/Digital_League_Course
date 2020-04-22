import xgboost as xgb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import roc_auc_score

from sklearn.model_selection import cross_val_score


#######
df_train = pd.read_csv('../train.csv')
df_test = pd.read_csv('../test.csv')

df_train.drop('ID_code', axis=1, inplace=True)
df_test.drop('ID_code', axis=1, inplace=True)

features_diff = ['var_0', 'var_2', 'var_6', 'var_9', 'var_12', 'var_13', 'var_22', 'var_26', 'var_40',
                 'var_44', 'var_53','var_76', 'var_80', 'var_81', 'var_86', 'var_94', 'var_95', 'var_108',
                 'var_109', 'var_110', 'var_112', 'var_115', 'var_123', 'var_131', 'var_133', 'var_139',
                 'var_146', 'var_148', 'var_164', 'var_165', 'var_166','var_174', 'var_177', 'var_179',
                 'var_131', 'var_180', 'var_184', 'var_188', 'var_131', 'var_190', 'var_191', 'var_195', 'var_198']

df_train['dif_mean'] = df_train[f_list].mean(axis=1)
df_train['dif_min'] = df_train[f_list].min(axis=1)
df_train['dif_max'] = df_train[f_list].max(axis=1)

df_train['dif_std'] = df_train[f_list].std(axis=1)
df_train['dif_median'] = df_train[f_list].median(axis=1)
df_train['dif_sum'] = df_train[f_list].sum(axis=1)


df_test['dif_mean'] = df_test[f_list].mean(axis=1)
df_test['dif_min'] = df_test[f_list].min(axis=1)
df_test['dif_max'] = df_test[f_list].max(axis=1)

df_test['dif_std'] = df_test[f_list].std(axis=1)
df_test['dif_median'] = df_test[f_list].median(axis=1)
df_test['dif_sum'] = df_test[f_list].sum(axis=1)

f_list = df_train.columns[1:]
df_train_target = df_train['target'].values

df_train_round = df_train[f_list].round(3)
df_test_round = df_test[f_list].round(3)

model = xgb.XGBClassifier(n_estimators=200, max_depth=4, eval_metric='auc')
scores = cross_val_score(model, df_train_round[f_list], df_train_target, scoring='roc_auc', cv=3)
print(scores)

## [0.83879685 0.83681562 0.84017592] - 50 estimators
## [0.86043873 0.86266555 0.86330935] -- n_estimators=100, max_depth=4
## [0.87239089 0.8742563  0.87685367] -- (n_estimators=200, max_depth=4)

#[0.85762741 0.85950723 0.86385151] (n_estimators=200, max_depth=3, eta=0.1)

# [0.87343381 0.87421892 0.87604229] (n_estimators=200, max_depth=4, eval_metric='auc')
# [0.87509478 0.87512236 0.87752895] (n_estimators=250, max_depth=4, eval_metric='auc')

model = xgb.XGBClassifier(n_estimators=200, max_depth=4, eval_metric='auc')
model.fit(df_train_round[f_list], df_train_target)

preds = model.predict(df_test_round[f_list])

sub_df = pd.DataFrame({"ID_code": df_test["ID_code"].values})
sub_df["target"] = preds
sub_df.to_csv("submission.csv", index=False)