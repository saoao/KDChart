/****************************************************************************
** Copyright (C) 2001-2020 Klaralvdalens Datakonsult AB.  All rights reserved.
**
** This file is part of the KD Chart library.
**
** Licensees holding valid commercial KD Chart licenses may use this file in
** accordance with the KD Chart Commercial License Agreement provided with
** the Software.
**
**
** This file may be distributed and/or modified under the terms of the
** GNU General Public License version 2 and version 3 as published by the
** Free Software Foundation and appearing in the file LICENSE.GPL.txt included.
**
** This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
** WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
**
** Contact info@kdab.com if any conditions of this licensing are not
** clear to you.
**
**********************************************************************/

#ifndef KDCHARTPERCENTBARDIAGRAM_P_H
#define KDCHARTPERCENTBARDIAGRAM_P_H


#include "KDChartBarDiagram_p.h"

namespace KDChart {

    class PercentBarDiagram : public BarDiagram::BarDiagramType
    {
    public:
        explicit PercentBarDiagram( BarDiagram* );
        ~PercentBarDiagram() override {}
        BarDiagram::BarType type() const override;
        const QPair<QPointF,  QPointF> calculateDataBoundaries() const override;
        void paint( PaintContext* ctx ) override;
    };

}

#endif
