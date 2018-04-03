library(readr)
library(dplyr)
library(tidyr)
library(ggplot2)

start = as.Date('2016-06-01')
end = as.Date('2019-06-01')
data = readr::read_csv("/repos/tutorial/resultats-levels-.csv")
data = data %>% mutate(Period = as.Date(paste(Period, '-01', sep=""), '%Y-%m-%d'))
cdata = data %>% mutate(Value = Value*ifelse(Variable == 'aide_logement_base_ressources', 1/12, 1))
ddata = cdata %>% spread(Variable, Value) %>% mutate(ressources = aide_logement + salaire_net + ppa)
edata = ddata %>% gather(Variable, Value, -Situation, -Reform, -Period)

# Zoom sur 2017 année post changement de situation
fdata = edata %>% filter(as.Date('2017-01-01') <= Period, Period <= as.Date('2019-03-01'), (Variable %in% c('aide_logement', 'aide_logement_base_ressources')))
ggplot(fdata, aes(x=Period, y=Value, group=Reform, color=Reform)) + geom_line() + facet_grid(Variable~Situation, scales="free")

# Salaire une longue période
gdata = edata %>% filter(start <= Period, Period <= end, (Variable %in% c('salaire_net')))
ggplot(gdata, aes(x=Period, y=Value, group=Reform, color=Reform)) + geom_line() + facet_grid(Variable~Situation, scales="free")

# Ressources et ces composantes pour le scénario rupture_2017
idata = edata %>% filter(as.Date('2017-01-01') <= Period, Period <= as.Date('2018-01-01'), (Situation %in% c('rupture_2017')), (Variable %in% c('aide_logement', 'ppa', 'ressources')))
ggplot(idata, aes(x=Period, y=Value, group=Reform, color=Reform)) + geom_line() + facet_grid(Variable~Situation, scales="free")

ldata = readr::read_csv("/repos/tutorial/resultats-levels-.csv")
mdata = ldata %>% filter(Variable %in% c('salaire_net', 'aide_logement'), Period=='2018-01', Reform == 'Base')
ndata = mdata %>% spread(Variable, Value)
ggplot(ndata, aes(x=salaire_net, y=aide_logement, group=Period)) + geom_line()
